# Copyright (c) 2011 gocept gmbh & co. kg
# See also LICENSE.txt

from setuptools import setup, find_packages
import sys

install_requires = [
    'setuptools',
]

if sys.version_info < (2, 7):
    install_requires.append('unittest2')


setup(
    name='gocept.jslint',
    version='1.0.1',
    author='Wolfgang Schnerring',
    author_email='ws@gocept.com',
    url='http://pypi.python.org/pypi/gocept.jslint',
    description="""\
Python-unittest integration for jslint.
""",
    long_description=(
        open('README.txt').read()
        + '\n\n'
        + open('CHANGES.txt').read()),
    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    license='ZPL',
    namespace_packages=['gocept'],
    install_requires=install_requires,
    extras_require=dict(test=[
        'mock',
    ]),
    entry_points=dict(console_scripts=[
        'jslint = gocept.jslint.util:run_jslint',
    ]),
)
