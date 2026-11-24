"""Validate generated root-hosted site links without network requests."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
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
if errors: print('\n'.join(errors)); sys.exit(1)
print('All generated local href/src targets exist.')
