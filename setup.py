# coding: utf-8
import os
import sys

from setuptools import setup


__author__ = 'Yeongbin Jo <yeongbin.jo@pylab.co>'


with open('README.md') as readme_file:
    long_description = readme_file.read()


# 'setup.py publish' shortcut.
if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist bdist_wheel')
    os.system('twine upload dist/*')
    sys.exit()
elif sys.argv[-1] == 'clean':
    import shutil
    if os.path.isdir('build'):
        shutil.rmtree('build')
    if os.path.isdir('dist'):
        shutil.rmtree('dist')
    if os.path.isdir('pyautogecko.egg-info'):
        shutil.rmtree('pyautogecko.egg-info')


setup(
    name="pyautogecko",
    version="0.1.3",
    author="Yeongbin Jo",
    author_email="narkopolo@riseup.net",
    description="Automatically install geckodriver that supports the currently installed version of Firefox.",
    license="MIT",
    keywords="geckodriver firefox selenium splinter",
    url="https://github.com/narkopolo/pyautogecko",
    packages=['pyautogecko'],
    entry_points={
        'console_scripts': ['geckodriver-path=pyautogecko.utils:print_geckodriver_path'],
    },
    long_description_content_type='text/markdown',
    long_description=long_description,
    python_requires='>=3',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Topic :: Software Development :: Testing',
        'Topic :: System :: Installation/Setup',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
)
