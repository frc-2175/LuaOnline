#!/usr/bin/env python3

import os
import random
import shutil
import string

shutil.rmtree('dist', ignore_errors=True)

print('Building dist folder...')
os.makedirs('dist', exist_ok=True)

buildId = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8)) # so beautiful. so pythonic.

root = 'src/index.html'
assets = [
    'src/dark.png',
    'src/fengari-web.js',
    'src/light.png',
    'src/tachyons.css',
]

rootContents = open(root).read()

def addId(filename):
    parts = filename.split('.')
    parts.insert(-1, buildId)
    return '.'.join(parts)

for asset in assets:
    basename = os.path.basename(asset)
    newFilename = addId(basename, buildId)
    shutil.copy(asset, 'dist/{}'.format(newFilename))

    rootContents = rootContents.replace(basename, newFilename)

shutil.copytree('src/monaco', 'dist/monaco')

with open('dist/index.html', 'w') as f:
    f.write(rootContents)
