import os, glob

h_code = os.path.expandvars('%APPDATA%/Code/User/History')
h_cursor = os.path.expandvars('%APPDATA%/Cursor/User/History')

candidates = []
for h in [h_code, h_cursor]:
    for path in glob.glob(h + '/**/*', recursive=True):
        if os.path.isfile(path) and not path.endswith('.json'):
            try:
                st = os.stat(path)
                with open(path, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                    lines = content.splitlines()
                    # Check if this looks like a python file and checking for number of lines
                    if len(lines) > 1500 and 'def extract_medications' in content and 'app = FastAPI' in content:
                        candidates.append((st.st_mtime, path, len(lines)))
            except Exception:
                pass

if candidates:
    best = sorted(candidates, key=lambda x: x[0], reverse=True)[0]
    import shutil
    shutil.copy2(best[1], 'e:/DScribe/recovered_main.py')
    print('Recovered file to e:/DScribe/recovered_main.py. Modified time:', best[0], 'Lines:', best[2], 'Path:', best[1])
else:
    print('No valid history files found with >= 1500 lines.')
