@echo off
REM Build a single-file Windows exe using PyInstaller
python -m pip install --upgrade pip
pip install -r requirements.txt
pyinstaller --noconfirm --onefile --windowed VO2Maxcalc.py
if exist dist\VO2Maxcalc.exe (
  echo Build complete. Executable is at dist\VO2Maxcalc.exe
) else (
  echo Build failed. Check the PyInstaller output above.
)
