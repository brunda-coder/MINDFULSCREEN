#!/usr/bin/env python3
"""
launcher.py — small CLI for launching Etherea MVP and dev utilities.
Usage:
    python launcher.py run
    python launcher.py deps    # prints recommended install commands
"""

import sys
import subprocess
from pathlib import Path

ROOT = Path(__file__).parent

def run():
    print("Starting Etherea Living OS (MVP)...")
    subprocess.run([sys.executable, str(ROOT / "main.py")])

def deps():
    print("Recommended install (virtualenv):")
    print("  python -m venv .venv && source .venv/bin/activate")
    print("  pip install -r requirements.txt")

def tree():
    for p in sorted(ROOT.rglob("*")):
        print(p.relative_to(ROOT))

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python launcher.py [run|deps|tree]")
        sys.exit(1)
    cmd = sys.argv[1]
    if cmd == "run":
        run()
    elif cmd == "deps":
        deps()
    elif cmd == "tree":
        tree()
    else:
        print("Unknown command:", cmd)
        sys.exit(1)
