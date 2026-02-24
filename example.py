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
