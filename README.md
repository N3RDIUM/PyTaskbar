# TbProgressLib
### The ultimate taskbar progress python package!

![](https://img.shields.io/github/downloads/somePythonProgrammer/PyTaskbar/total)
![](https://img.shields.io/github/license/somePythonProgrammer/PyTaskbar)

[Docs Here!](https://github.com/somePythonProgrammer/PyTaskbar/blob/main/docs.md)

#### Want to get taskbar progress hassle free?

#### Just run the install.py file with your python, and copy the TaskbarLib.tlb file to your project directory!

#### It works for both terminals and GUIs!

#### Then use it by adding this line: 
        import tbprog

## requirements:

        comtypes
        PyGetWindow
        

## example:

        import time
        import tbprog

        prog = tbprog.Progress()
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


## **installation**
[click here](https://github.com/somePythonProgrammer/TbProgressLib/blob/main/docs.md#installation)
# _______________________________________________________________________
### Please let me know if there are any problems in the Issues tab.

### Happy Coding!
