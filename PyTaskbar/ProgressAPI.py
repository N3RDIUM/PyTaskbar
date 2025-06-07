import ctypes
import comtypes.client as cc
import sys

parent_dir = __file__.rsplit("\\", 1)[0]
sys.path.append(parent_dir)
cc.GetModule("./TaskbarLib.tlb")

import comtypes.gen.TaskbarLib as tbl
from comtypes.gen import _683BF642_E9CA_4124_BE43_67065B2FA653_0_1_0

taskbar = cc.CreateObject(
    "{56FDF344-FD6D-11d0-958A-006097C9A090}",
    interface=tbl.ITaskbarList3) 


# Progress types
NORMAL = 0
WARNING = 10
ERROR = 15
LOADING = -15
DONE = 1

PROGRESS_TYPES = [
    NORMAL,
    WARNING,
    ERROR,
    LOADING,
    DONE
]

class Progress:
    def __init__(self, hwnd: int | None = None):
        super().__init__()

        if hwnd is None:
            hwnd = ctypes.windll.kernel32.GetConsoleWindow()
        self.window_handle = hwnd

        taskbar.ActivateTab(hwnd)
        taskbar.HrInit()

    def set_progress(self, value: int, max: int = 100):
        if type(value) != int:
            raise TypeError(f"Progress.set_progress: expected `value` to be type int, not {type(value)}")
        if value < 0:
            raise Exception(f"Progress.set_progress: `value` is less than zero: {value} < 0")
        if value > max:
            raise Exception(f"Progress.set_progress: `value` is greater than max: {value} > {max}")

        taskbar.setProgressValue(self.window_handle, value, max)

    def set_progress_type(self, progress_type: int):
        if type(progress_type) != int:
            raise TypeError(f"Progress.set_progress_type: expected `progress_type` to be type int, not {type(progress_type)}")
        if progress_type not in PROGRESS_TYPES:
            raise TypeError(f"Progress.set_progress_type: expected `progress_type` to be one of [NORMAL, WARNING, ERROR, LOADING, DONE], not {progress_type}")

        taskbar.SetProgressState(self.window_handle, progress_type)
    
    def flash_done(self):
        ctypes.windll.user32.FlashWindow(self.window_handle, True)

    def reset(self):
        self.set_progress_type(NORMAL)
        self.set_progress(0)

