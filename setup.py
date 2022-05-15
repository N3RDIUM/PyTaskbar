from turtle import down
import setuptools
import sys
import shutil

setuptools.setup(
    name='PyTaskbarProgress',
    version='0.0.8',
    author='somePythonProgrammer',
    description='The ultimate taskbar progress python package!',
    packages = setuptools.find_packages(include=['PyTaskbar']),
    package_dir={'PyTaskbarProgress': 'PyTaskbar'},
    classifiers = [
        'License :: OSI Approved :: MIT License',
        'Operating System :: Microsoft :: Windows :: Windows 10',
    ],
    python_requires='>=3.6',
    install_requires=[
        'comtypes',
        'pygetwindow',
        'setuptools',
    ],
    include_package_data=True,
    url = 'https://github.com/somePythonProgrammer/PyTaskbar',
    long_description_content_type='text/markdown',
    long_description=open('README.md').read(),
    zip_safe=False,
    download_url='https://github.com/somePythonProgrammer/PyTaskbar/archive/refs/tags/0.0.8.tar.gz'
)
