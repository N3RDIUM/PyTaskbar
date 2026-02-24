import time
import PyTaskbar
from PyTaskbar import NORMAL, WARNING, ERROR, LOADING

progress = PyTaskbar.Progress()

# Loading animation
progress.set_progress_type(LOADING)
time.sleep(5)

# Show normal (green) progress
progress.set_progress_type(NORMAL)
for i in range(100):
    progress.set_progress(i)
    time.sleep(0.05)

# Make the progress bar yellow
progress.set_progress_type(WARNING)
progress.set_progress(42)
time.sleep(2)

# Make the progress bar red
progress.set_progress_type(ERROR)
progress.set_progress(42)
time.sleep(2)

# Flash the taskbar icon
progress.flash_done()
time.sleep(5)
