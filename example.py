import time
import PyTaskbarProgress

prog = PyTaskbarProgress.Progress()
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
