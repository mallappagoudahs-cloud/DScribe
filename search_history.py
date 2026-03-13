import os, glob

h_code = os.path.expandvars('%APPDATA%/Code/User/History')
h_cursor = os.path.expandvars('%APPDATA%/Cursor/User/History')

# Just find ALL files in history that contain 'app = FastAPI'
candidates = []
for h in [h_code, h_cursor]:
    for path in glob.glob(h + '/**/*', recursive=True):
        if os.path.isfile(path) and not path.endswith('.json'):
            try:
                st = os.stat(path)
                with open(path, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                    lines = content.splitlines()
                    if 'app = FastAPI' in content:
                        candidates.append((st.st_mtime, path, len(lines)))
            except Exception:
                pass

if candidates:
    best = sorted(candidates, key=lambda x: x[0], reverse=True)[0]
    for c in sorted(candidates, key=lambda x: x[0], reverse=True)[:5]:
        print(f'MTime: {c[0]}, Lines: {c[2]}, Path: {c[1]}')
else:
    print('No FastAPI history files found at all.')

print('\nNow searching for HTML history files...')
html_candidates = []
for h in [h_code, h_cursor]:
    for path in glob.glob(h + '/**/*', recursive=True):
        if os.path.isfile(path) and not path.endswith('.json'):
            try:
                st = os.stat(path)
                with open(path, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                    lines = content.splitlines()
                    if 'id="processBtn"' in content or 'dropZone' in content:
                        html_candidates.append((st.st_mtime, path, len(lines)))
            except Exception:
                pass

if html_candidates:
    best = sorted(html_candidates, key=lambda x: x[0], reverse=True)[0]
    for c in sorted(html_candidates, key=lambda x: x[0], reverse=True)[:5]:
        print(f'MTime: {c[0]}, Lines: {c[2]}, Path: {c[1]}')
else:
    print('No HTML history files found at all.')
