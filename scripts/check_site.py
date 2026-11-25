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
    if not re.search(r'/assets/css/professional\.css\?v=\d+',p.read_text(encoding='utf-8')):
        errors.append(f'{p}: missing versioned presentation stylesheet')
# Every project must expose a direct Resume source link and topic photography.
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
        if '/assets/images/photos/' not in html:
            errors.append(f'{p}: missing topic photograph')
if errors: print('\n'.join(errors)); sys.exit(1)
catalog=json.loads(Path('_data/portfolio.json').read_text(encoding='utf-8'))
if len({p['slug'] for p in catalog}) != len(catalog) or len({p['url'] for p in catalog}) != len(catalog):
    errors.append('Project catalog must have one canonical entry and URL per project')
index=(ROOT/'all_posts.html').read_text(encoding='utf-8')
if index.count('class="catalog-item"') != len(catalog):
    errors.append('Project index must include each canonical project once before JavaScript runs')
for item in catalog:
    target=ROOT/item['url'].lstrip('/')
    if not target.exists() or item['url'] not in index or item['github'] not in index:
        errors.append(f"Catalog entry is missing its article or source link: {item['slug']}")
for p in ROOT.rglob('*.html'):
    if re.search(r'(?i)\btwo (?:undergraduate degrees|undergrads|publications|master.s degrees)',p.read_text(encoding='utf-8')):
        errors.append(f'{p}: counted credentials must be replaced by named education/publications')
home=(ROOT/'index.html').read_text(encoding='utf-8')
for required in ['hero-grid','role-description','tiles interactive-projects','Master’s in Machine Learning','Master’s in Business Analytics','/aboutme.html']:
    if required not in home: errors.append(f'Homepage missing professional presentation element: {required}')
if 'class="proof-section"' in home or 'Two master' in home:
    errors.append('Homepage must explain role and degrees without a standalone KPI strip')
if home.count('class="tile-cta"') != 6 or len(re.findall(r'<img[^>]+src="/assets/images/photos/', home)) != 6:
    errors.append('Homepage must expose six photographic interactive project tiles')
for name in ['forecasting','knowledge-search','commercial-reporting']:
    html=(ROOT/'work'/f'{name}.html').read_text(encoding='utf-8')
    if 'technical-detail' not in html or '<pre' not in html or '<summary>' not in html:
        errors.append(f'{name}: technical walkthrough did not render as expandable code')
    if re.search(r'(?m)^```|^#{2,4} ',html):
        errors.append(f'{name}: unrendered Markdown in case study')
profile=(ROOT/'aboutme.html').read_text(encoding='utf-8')
for required in ['Machine Learning','Business Analytics','Engineering Sciences','Industrial Civil Engineering','Selected publications']:
    if required not in profile: errors.append(f'Profile missing qualification: {required}')
if errors: print('\n'.join(errors)); sys.exit(1)
print(f'Local targets exist; all {len(project_sources)} project sources register GitHub evidence and topic photographs.')
