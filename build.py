import zipfile, os

includes = [
    '__init__.py', 'action.py', 'config.py', 'dialogs.py',
    'mobi_stuff.py', 'utilities.py',
    'plugin-import-name-kindleunpack_plugin.txt',
]

with zipfile.ZipFile('KindleUnpack-ZIP-mod.zip', 'w', zipfile.ZIP_DEFLATED) as zf:
    for fname in includes:
        if os.path.exists(fname):
            zf.write(fname)
    for root, dirs, files in os.walk('images'):
        for f in files:
            zf.write(os.path.join(root, f))
    for root, dirs, files in os.walk('kindleunpackcore'):
        dirs[:] = [d for d in dirs if d not in {'.git', '__pycache__'}]
        for f in files:
            if f.endswith('.py'):
                zf.write(os.path.join(root, f))
    if os.path.exists('translations'):
        for root, dirs, files in os.walk('translations'):
            for f in files:
                zf.write(os.path.join(root, f))

print('Created: KindleUnpack-ZIP-mod.zip')
