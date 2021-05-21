# TbProgressLib
### The ultimate taskbar progress python package!

![](https://img.shields.io/github/downloads/somePythonProgrammer/PyTaskbar/total)
![](https://img.shields.io/github/license/somePythonProgrammer/PyTaskbar?label=license)

[Docs Here!](https://github.com/somePythonProgrammer/PyTaskbar/blob/main/docs.md)

#### Works for both terminals and GUIs!

## Requirements:

        comtypes
        PyGetWindow
        

## Example:

        import time
        import PyTaskbar

        prog = PyTaskbar.Progress()
        prog.init()

        prog.setState('loading')
        time.sleep(5)

        prog.setState('normal')

        for i in range(100):
            prog.setProgress(i)
            time.sleep(0.05)
        prog.setProgress(0)

        prog.setState('warning')

        for i in range(100):
            prog.setProgress(i)
            time.sleep(0.05)

        prog.setProgress(0)
        prog.setState('error')

        for i in range(100):
            prog.setProgress(i)
            time.sleep(0.05)

        prog.setProgress(0)

        prog.setState('done')
        while True:
            time.sleep(1)
            print('close me!')


## **Installation**
[click here](https://github.com/somePythonProgrammer/TbProgressLib/blob/main/docs.md#installation)
<HR>

### Happy Coding!
