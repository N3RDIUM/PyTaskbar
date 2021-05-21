import os
import shutil
os.system('cd '+os.path.join('.'))
os.system('python setup.py install')
print('\n\n\nNOTE: Copy the TaskbarLib.tlb file to your project directory')
print('\nRunning the example for a quick test,hang on...')
os.system('python example.py')
