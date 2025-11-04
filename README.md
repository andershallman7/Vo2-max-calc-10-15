# VO2 Max Calculator

A tiny app that estimates VO₂ max from your age and resting heart rate (RHR). This repository includes a Tkinter GUI and packaging helpers so you can download a single-file Windows executable (.exe) and run the app by double-clicking.

Files added:

- `VO2Maxcalc.py` — Tkinter GUI application (entrypoint)
- `requirements.txt` — build dependency (PyInstaller)
- `build_exe.bat` — convenient Windows build script (uses PyInstaller)
- `build_exe.sh` — build script for other OSes (note: building a Windows .exe requires Windows)
- `.github/workflows/build-windows.yml` — GitHub Actions workflow to build the Windows exe and upload it as an artifact

Quick start (downloaded exe):

1. Go to the GitHub repository's Actions tab and open the latest `Build Windows executable` run.
2. Download the artifact `VO2Maxcalc-windows`.
3. Unzip and double-click `VO2Maxcalc.exe` — the GUI will open.

Build locally on Windows (produces a double-clickable exe):

1. Install Python 3.8+ for Windows (include Tcl/Tk).
2. Open a Command Prompt in this repo and run:

```bat
build_exe.bat
```

The resulting `dist\VO2Maxcalc.exe` can be distributed as a single file.

Build on Linux/macOS (creates native binary for that OS):

```bash
./build_exe.sh
```

Notes:

- PyInstaller must be run on the target OS to create a native executable for that OS (you cannot make a Windows .exe from Linux using PyInstaller unless using Wine).
- tkinter is included with the standard Python installer on Windows; no extra packages are required at runtime.

Usage:

1. Run the app (double-click the exe or run `python VO2Maxcalc.py`).
2. Enter your age and resting heart rate.
3. Click "Calculate VO₂ Max" and the estimated result will be shown.

If you'd like, I can also:

- Add icons and version metadata for the Windows exe.
- Create a small installer (Inno Setup) to package the exe with a shortcut.
- Publish a prebuilt release and attach the exe on GitHub releases.

