# Welcome to the TbProgressLib documentation!
![](https://img.shields.io/github/downloads/somePythonProgrammer/TbProgressLib/total)
![](https://img.shields.io/github/license/somePythonProgrammer/TbProgressLib)

### The ultimate taskbar progress python package!

## index
Quick Start:
    [installation](#installation)
    [example](#example)
    
API Docs: [The main object](#main_object)

## **installation**

Unfortunately, I did not upload this to Pypi, so you cannot install it with pip.

To install:

1.Download or clone this repository.

2.If you have downloaded it, unzip the downloaded file.

3.Go to file explorer and get to the directory where you have cloned or unzipped the repository.

4.type 'cmd' in the place where you see the path.

![image](https://user-images.githubusercontent.com/74598401/114820157-33103c00-9ddc-11eb-9786-946ad2c0973c.png)

5.hit enter.

6.type 'python install.py' and hit enter (If you have python on your PATH variable. If not, add it.)

7.copy 'TaskbarLib.tlb' to your project directory.

8.Try out the example now!

##### [back to top](#index)
##### [API docs](#main_object)

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
    
##### [back to top](#index)
##### [API docs](#main_object)

### _______________________________________________________
## main_object
#### the main object:
##### _+ TaskbarProgress()
##### _____+ functions
##### _________+ __init__(hwnd=hWnd) (called when you create the object, if hwnd is not given,this will automatically take the hwnd of the cmd window.)
##### _________+ init() (initialise the object to display progress)
##### _________+ setState(value:string) (one of normal,warning,error,loading or done) [more](#setState)
##### _________+ setProgress(value:int,max=100) (set taskbar progress value) [more](#setProgress)
##### [back to top](#index)

## setState
##### _+ the main function: TaskbarProgress.setState

###### _____+ setState(value)
###### _________+ value: string (one of normal,warning,error,loading or done)
###### _________+ usage example:
##### [back to top](#index)
##### [back to API docs](#main_object)

    import tbprog
    import time
    
    progress = Progress()
    progress.init()
    
    #taskbar icon becoms green, or starts to display a loading animation
    progress.setState('loading')
    time.sleep(5)
    
    #progress becomes yellow
    progress.setState('warning')
    time.sleep(5)
    
    #progress becomes red
    progress.setState('error')
    time.sleep(5)
    
    #taskbar icon is normal again!
    progress.setState('normal')

## setProgress
##### _+ the main function: TaskbarProgress.setProgress

###### _____+ setProgress(value,max)
###### _________+ value: integer (set the numerator of the taskbar progress value)
###### _________+ value: integer (set the denominator of the taskbar progress value)
###### _________+ usage example:
##### [back to top](#index)
##### [back to API docs](#main_object)

    import tbprog
    import time
    
    progress = Progress()
    progress.init()
    
    for i in range(100):
        progress.setProgress(i,100)
        
### Happy Coding!
