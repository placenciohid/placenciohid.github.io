"""Validate generated root-hosted site links without network requests."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
import json
import re
import sys
ROOT = Path('_site')
errors=[]
class Links(HTMLParser):
    def __init__(self, path): super().__init__(); self.path=path
    def handle_starttag(self, tag, attrs):
        attrs=dict(attrs)
        for key in ['href','src']:
            val=attrs.get(key,''); url=urlsplit(val)
            if not val or val.startswith('#') or url.scheme or url.netloc: continue
            dest=unquote(url.path)
            target=ROOT/dest.lstrip('/') if dest.startswith('/') else self.path.parent/dest
            if not target.exists(): errors.append(f'{self.path}: missing {val}')
if not ROOT.exists(): sys.exit('Build with Jekyll first')
for p in ROOT.rglob('*.html'):
    Links(p).feed(p.read_text(encoding='utf-8'))
# Every project must expose a direct Resume source link and topic illustration.
registry = json.loads(Path('_data/projects.json').read_text(encoding='utf-8'))
project_sources = list(Path('work').glob('*.md')) + list(Path('projects').glob('*.md')) + list(Path('_posts').glob('*.md'))
for source in project_sources:
    match = re.search(r'(?m)^project_id: (.+)$', source.read_text(encoding='utf-8'))
    if not match or match.group(1).strip() not in registry:
        errors.append(f'{source}: missing registered GitHub evidence')
for p in ROOT.rglob('*.html'):
    relative = p.relative_to(ROOT)
    if relative.parts[0] in {'work','projects'} or re.match(r'^\d{4}$', relative.parts[0]):
        html = p.read_text(encoding='utf-8')
        if 'class="project-evidence"' not in html or 'https://github.com/placenciohid/Resume/' not in html:
            errors.append(f'{p}: missing direct GitHub project evidence')
        if '/assets/images/topics/' not in html:
            errors.append(f'{p}: missing topic artwork')
if errors: print('\n'.join(errors)); sys.exit(1)
print(f'Local targets exist; all {len(project_sources)} project sources register GitHub evidence and topic artwork.')
