#!/usr/bin/env python3
import os
import subprocess
import sys

os.chdir(os.path.dirname(os.path.abspath(__file__)))
sys.exit(subprocess.call(["node", "server.js"]))
