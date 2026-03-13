import os, glob

h_code = os.path.expandvars('%APPDATA%/Code/User/History')
h_cursor = os.path.expandvars('%APPDATA%/Cursor/User/History')

candidates = []
for h in [h_code, h_cursor]:
    for path in glob.glob(h + '/**/*', recursive=True):
        if os.path.isfile(path) and not path.endswith('.json'):
            try:
                st = os.stat(path)
                if st.st_size > 50000: # ~1800 lines is around 60-70KB minimum
                    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
                        lines = f.readlines()
                        if len(lines) > 1750 and 'const TRANSLATIONS =' in ''.join(lines):
                            candidates.append((st.st_mtime, path, len(lines)))
            except Exception:
                pass

if candidates:
    best = sorted(candidates, key=lambda x: x[0], reverse=True)[0]
    import shutil
    shutil.copy2(best[1], 'e:/DScribe/static/recovered_best_index.html')
    print('Recovered file to e:/DScribe/static/recovered_best_index.html. Modified time:', best[0], 'Lines:', best[2], 'Path:', best[1])
else:
    print('No valid history files found with >= 1750 lines.')
