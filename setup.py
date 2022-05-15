import setuptools
import sys
import shutil

# Copy the PyTaskbar/TaskbarLib.tlb file to the dist folder

def copy_tlb(dst):
    shutil.copy("PyTaskbar\\TaskbarLib.tlb", dst)

sitepackages_path = sys.prefix + '\\Lib\\site-packages'
libpath = sitepackages_path + '\\PyTaskbar\\TaskbarLib.tlb'.replace('\\', '/')

setuptools.setup(
    name='PyTaskbar',
    version='0.0.1',
    author='somePythonProgrammer',
    description='The ultimate taskbar progress python package!',
    packages = setuptools.find_packages(include=['PyTaskbar']),
    package_dir={'PyTaskbar': 'PyTaskbar'},
    classifiers = [
        'License :: OSI Approved :: MIT License',
        'Operating System :: Microsoft :: Windows :: Windows 10',
    ],
    python_requires='>=3.6',
    install_requires=[
        'comtypes',
        'setuptools',
    ],
    include_package_data=True,
    url = 'https://github.com/somePythonProgrammer/PyTaskbar',
    long_description_content_type='text/markdown',
    long_description=open('README.md').read(),
)
