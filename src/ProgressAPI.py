import os
import ctypes
import comtypes.client as cc
from enum import Enum

# Load TaskbarLib.tlb
parent_dir = os.path.dirname(__file__)
cc.GetModule(os.path.join(parent_dir, "TaskbarLib.tlb"))
import comtypes.gen.TaskbarLib as taskbarlib

taskbar = cc.CreateObject(
    "{56FDF344-FD6D-11d0-958A-006097C9A090}", interface=taskbarlib.ITaskbarList3
)


class ProgressType(Enum):
    """Taskbar progress type flags.

    Attributes:
        NOPROGRESS: No progress is displayed (clears progress bar).
        INDETERMINATE: Marquee-style progress (unknown duration).
        NORMAL: Normal progress (green).
        ERROR: Error state (red).
        PAUSED: Paused state (yellow).
    """

    NOPROGRESS = 0
    INDETERMINATE = 1
    NORMAL = 2
    ERROR = 4
    PAUSED = 8


class TaskbarProgress:
    """Provides methods to interact with the windows taskbar progress API."""

    _hwnd: int

    def __init__(self, hwnd: int | None = None):
        """Initialize the taskbar API.

        Params:
            hwnd(int): Window handle of the target window
        """

        self._hwnd = (
            hwnd if hwnd is not None else ctypes.windll.kernel32.GetConsoleWindow()
        )
        taskbar.HrInit()

    def set_progress(self, value: int, max: int = 100):
        """Set the taskbar progress of the target window.

        Params:
            value(int): The progress value (0 < value < max)
            max(int): The maximum progress value
        """

        if value < 0:
            raise Exception(f"`value`={value} is less than zero")
        if value > max:
            raise Exception(f"`value`={value} greater than `max`={max}")

        taskbar.setProgressValue(self._hwnd, value, max)

    def set_progress_type(self, flag: ProgressType):
        """Set the progress type flag. See enum ProgressType for more."""

        taskbar.SetProgressState(self._hwnd, flag.value)

    def flash_done(self):
        """Flash the taskbar icon to indicate that the task completed. This will reset the progress state!"""

        self.reset()
        ctypes.windll.user32.FlashWindow(self._hwnd, True)

    def reset(self):
        """Reset the progress value and type."""

        self.set_progress_type(ProgressType.NORMAL)
        self.set_progress(0)
