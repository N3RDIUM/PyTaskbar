# PyTaskbar
The ultimate taskbar progress python package!

## About
This is a wrapper API around the TaskbarLib.tlb (Windows 7+) that makes it easy
to show progress in the taskbar icon, a great plus when it comes to UX for your
desktop/TUI application. Simple API, works with any GUI framework!

## Installation
This package is available on PyPI! For most cases, installation is as simple as:
```
pip install PyTaskbar
```

If you want to install latest git instead:
```
pip install git+https://github.com/N3RDIUM/PyTaskbar.git
```

## Usage
Here's a minimal usage example:

```python
import time
from PyTaskbar import TaskbarProgress, ProgressType

# This will target the terminal window.
progress = TaskbarProgress()

# If you're using a GUI framework, pass the target window handle like so:
# progress = TaskbarProgress(window_handle)

# No progress
progress.set_progress_type(ProgressType.NOPROGRESS)
time.sleep(3)

# Indeterminate progress state
progress.set_progress_type(ProgressType.INDETERMINATE)
time.sleep(3)

# Normal (green) progress
progress.set_progress_type(ProgressType.NORMAL)
for i in range(100):
    progress.set_progress(i)
    time.sleep(0.05)

# Paused (yellow) progress
progress.set_progress_type(ProgressType.PAUSED)
progress.set_progress(42)
time.sleep(2)

# Error (red) progress
progress.set_progress_type(ProgressType.ERROR)
progress.set_progress(42)
time.sleep(2)

# Flash the taskbar icon signalling that the task completed
progress.flash_done()
time.sleep(5)
```

## Thanks and citations
- [@timminator](https://github.com/timminator) for helping fix the minimize bug

