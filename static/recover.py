import os, glob

h_code = os.path.expandvars('%APPDATA%/Code/User/History')
h_cursor = os.path.expandvars('%APPDATA%/Cursor/User/History')

candidates = []
for h in [h_code, h_cursor]:
    for path in glob.glob(h + '/**/*', recursive=True):
        if os.path.isfile(path) and not path.endswith('.json'):
            try:
                st = os.stat(path)
                if st.st_size > 50000: # index.html is likely > 50KB
                    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
                        if 'const TRANSLATIONS =' in f.read():
                            candidates.append((st.st_mtime, path))
            except Exception:
                pass

if candidates:
    best = sorted(candidates, key=lambda x: x[0], reverse=True)[0]
    import shutil
    shutil.copy2(best[1], 'e:/DScribe/static/recovered_index.html')
    print('Recovered the most recent version to recovered_index.html. Modified time:', best[0])
    with open(best[1], 'r', encoding='utf-8', errors='ignore') as f:
        print('Lines in best file:', len(f.read().splitlines()))
else:
    print('No valid history files found.')
