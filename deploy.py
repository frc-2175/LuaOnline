#!/usr/bin/env python3

import subprocess

subprocess.run(['ssh', 'bvisness', 'rm -rf apps/lua'])
subprocess.run(['scp', '-r', 'dist', 'bvisness:apps/lua'])
