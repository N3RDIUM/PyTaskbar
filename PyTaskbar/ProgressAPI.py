import ctypes

import comtypes.client as cc
import sys
import warnings


parent_dir = __file__.rsplit("\\", 1)[0]
sys.path.append(parent_dir)
cc.GetModule("./TaskbarLib.tlb")

import comtypes.gen.TaskbarLib as tbl
from comtypes.gen import _683BF642_E9CA_4124_BE43_67065B2FA653_0_1_0
taskbar = cc.CreateObject(
    "{56FDF344-FD6D-11d0-958A-006097C9A090}",
    interface=tbl.ITaskbarList3) 

hWnd = ctypes.windll.kernel32.GetConsoleWindow()
taskbar.ActivateTab(hWnd)

class Progress(object):
    def __init__(self,hwnd=hWnd):
        super().__init__()
        self.initialised = False
        self.state = None
        self.win = hwnd

    def init(self):
        self.thisWindow = self.win
        taskbar.ActivateTab(self.win)
        taskbar.HrInit()
        self.state = 'normal'
        self.progress = 0
        self.initialised = True

    def setState(self,value):
        if not self.initialised == False:
            if value == 'normal':
                taskbar.SetProgressState(self.thisWindow,0)
                self.state = 'normal'

            elif value == 'warning':
                taskbar.SetProgressState(self.thisWindow,10)
                self.state = 'warning'

            elif value == 'error':
                taskbar.SetProgressState(self.thisWindow,15)
                self.state = 'error'

            elif value == 'loading':
                taskbar.SetProgressState(self.thisWindow,-15)
                self.state = 'loading'
            
            elif value == 'done':
                ctypes.windll.user32.FlashWindow(self.thisWindow,True)
                self.state = 'done'
            
            else:
                warnings.warn('Invalid Argument {} .Please selece one from (normal,warning,error,loading,done).'.format(value))

        else:
            warnings.warn('Please initialise the object (method:Progress.initialise())')

    def setProgress(self,value:int):
        if not self.initialised == False:
            taskbar.setProgressValue(self.thisWindow,value,100)

        elif value>100 or value<0:
            warnings.warn('Invalid Argument {} .Please selece one from (<100,>0).'.fromat(value))

        else:
            warnings.warn('Please initialise the object (method:Progress.initialise())')