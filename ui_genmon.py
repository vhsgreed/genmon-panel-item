#!/usr/bin/env python3
"""XFCE genmon panel item — one line, refreshed by genmon every 60s.

Panel setup (XFCE):
  1. Install xfce4-genmon-plugin (e.g. `sudo apt install xfce4-genmon-plugin`).
  2. Right-click panel -> Panel -> Add New Items -> "Generic Monitor".
  3. Properties:
       Command:  python3 path/to/ui_genmon.py
       Period:   60
       Label:    (empty)
  4. Font: a monospace font keeps the sparkline aligned.

Windows later: swap this module for ui_windows.py (same core, tray rendering).
"""
import os
import sys

# allow running directly from genmon without installing
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from linktrack.cli import panel_line

if __name__ == "__main__":
    try:
        print(panel_line(fetch_first=True))
    except Exception as e:  # never let the panel show a crash
        print(f"LINK err: {e}")
        sys.exit(0)
