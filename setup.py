import setuptools

setuptools.setup(
    name='PyTaskbar',
    version='0.1.0',
    author='N3RDIUM',
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
        'pygetwindow',
        'setuptools',
    ],
    include_package_data=True,
    url = 'https://github.com/N3RDIUM/PyTaskbar',
    long_description_content_type='text/markdown',
    long_description=open('README.md').read(),
    zip_safe=False,
    # download_url='https://github.com/N3RDIUM/PyTaskbar/archive/refs/tags/0.0.8.tar.gz'
)
