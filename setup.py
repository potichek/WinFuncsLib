import setuptools

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name='WinFuncs',
    version='0.0.1',
    author='potichek',
    author_email='bibilmeshka@gmail.com',
    description='Simplifying various WinAPI functions, with this library you won`t need to use ctypes to call WinAPI functions.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/myusername/mypackage',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    install_requires=[
        'somepackage>=1.1.0',
    ]
)