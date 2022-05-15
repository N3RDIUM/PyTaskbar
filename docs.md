# Welcome to the TbProgressLib documentation!
![](https://img.shields.io/github/downloads/somePythonProgrammer/PyTaskbar/total)
![](https://img.shields.io/github/license/somePythonProgrammer/PyTaskbar)

### The ultimate taskbar progress python package!

<A name='index'></A>

## Index
Quick Start:
    [installation](#docs_install)
    [example](#docs_example)
    
API Docs: [The Main Object](#main_object)

Contributing: [Contributing guidelines](https://github.com/somePythonProgrammer/PyTaskbar/blob/main/CONTRIBUTING.md)

<A name='docs_install'></A>

## **Installation**

You can install PyTaskbar with: 
```
pip install PyTaskbar
```

### To install with wheel:

1. Download wheel from this distribution:[LINK](https://github.com/somePythonProgrammer/PyTaskbar/releases/tag/0.0.1).

2. Do "pip install path-to-wheel.whl"

3. Try out the [example](#docs_example) now!

### To install manually:
1. Download wheel from this distribution:[LINK](https://github.com/somePythonProgrammer/PyTaskbar/releases/tag/0.0.1).

2. Once you have downloaded it, unzip the downloaded file.

3. Go to file explorer and get to the directory where you have cloned or unzipped the repository.

4. type 'cmd' in the place where you see the path.

![image](https://user-images.githubusercontent.com/74598401/119104885-69c01e80-ba3a-11eb-9c24-45eaf4bab5bf.png)

5. hit enter.

6. type 'python install.py' and hit enter.

8. Try out the [example](#docs_example) now!

##### [back to top](#index)
##### [API docs](#main_object)

<A name='docs_example'></A>

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
    
##### [back to top](#index)
##### [API docs](#main_object)

<HR>
<A name='main_object'></A>

## Main Object 
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

    import PyTaskbar
    import time
    
    progress = PyTaskbar.Progress()
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

    import PyTaskbar
    import time
    
    progress = PyTaskbar.Progress()
    progress.init()
    
    for i in range(100):
        progress.setProgress(i,100)
        
### Happy Coding!
