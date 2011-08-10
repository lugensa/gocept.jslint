# Copyright (c) 2011 gocept gmbh & co. kg
# See also LICENSE.txt

from setuptools import setup, find_packages


setup(
    name='gocept.jslint',
    version='0.2dev',
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
    install_requires=[
        'setuptools',
    ],
    extras_require=dict(test=[
        'mock',
    ]),
)
