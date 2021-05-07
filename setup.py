# Copyright (c) 2011-2021 gocept gmbh & co. kg
# See also LICENSE.txt

from setuptools import find_packages
from setuptools import setup


install_requires = [
    'setuptools',
]

setup(
    name='gocept.jslint',
    version='3.0',
    author='Wolfgang Schnerring',
    author_email='mail@gocept.com',
    url='https://github.com/gocept/gocept.jslint',
    description="""Python-unittest integration for jslint.""",
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Zope Public License',
        'License :: OSI Approved',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation',
        'Programming Language :: Python',
        'Topic :: Software Development :: Testing',
        'Topic :: Software Development',
    ],
    long_description=(
        open('README.rst').read()
        + '\n\n'
        + open('CHANGES.rst').read()),
    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    license='ZPL',
    namespace_packages=['gocept'],
    python_requires='>=3.6, <4',
    install_requires=install_requires,
    extras_require=dict(test=[
    ]),
    entry_points=dict(console_scripts=[
        'gocept-jshint = gocept.jslint.util:run_jslint',
    ]),
)
