#!/usr/bin/env bash
# NOTE: PyInstaller on Linux will produce a Linux executable. To produce a Windows .exe you must build on Windows
python3 -m pip install --upgrade pip
pip3 install -r requirements.txt
pyinstaller --noconfirm --onefile --windowed VO2Maxcalc.py
echo "Built executable (if running on this OS) in dist/"
