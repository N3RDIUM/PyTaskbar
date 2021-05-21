import setuptools

setuptools.setup(
    name='PyTaskbar',
    version='0.0.1',
    author='somePythonProgrammer',
    description='The ultimate taskbar progress python package!',
    packages = setuptools.find_packages(include=['PyTaskbar']),
    package_dir={'PyTaskbar': 'PyTaskbar'},
    classifiers = [
        'Programming Language :: Python :: 3',
        'Liscence :: OSI Approved :: MIT Licence',
        'Operating System :: Windows'
    ],
    python_requires='>=3.6',
    install_requires=[
        'comtypes',
        'setuptools',
    ]
)
