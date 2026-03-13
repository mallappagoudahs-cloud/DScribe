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
                    if 'import FastAPI' in content or 'from fastapi ' in content:
                        candidates.append((st.st_size, path, len(lines)))
            except Exception:
                pass

if candidates:
    best = sorted(candidates, key=lambda x: x[0], reverse=True)[0]
    for c in sorted(candidates, key=lambda x: x[0], reverse=True)[:5]:
        print(f'Size: {c[0]}, Lines: {c[2]}, Path: {c[1]}')
else:
    print('No python history files found at all.')
