=============
gocept.jslint
=============

This package integrates the JSHint code analysis tool (http://jshint.com) with
Python's unittest module. (The name is left over from when JSHint didn't exist
and only Douglas Crockford's JSLint was available.)

It provides a special JSLint-TestCase class that collects JavaScript files (in
a configurable manner) and dynamically generates a test method for each file
that calls jshint on that file.

To use it, create a test class like this::

    class MyJSLintTest(gocept.jslint.TestCase):

        include = ('my.package.browser:js',
                   'my.package.browser:js/lib')
        options = (gocept.jslint.TestCase.options +
                   ('browser', 'jquery',))


``include`` is a list of "resource paths" of the form ``packagename:path``
(passed to pkg_resources).

``options`` is a list of arguments that are passed to JSHint (see its
`documentation`_ for details).

.. _documentation: http://www.jshint.com/options/

``predefined`` is a list of global names that should be considered predefined
(for use with the ``undef`` option).

``exclude`` can be a list of filenames (without path) that will not be
collected.

All files ending in ``.js`` contained in each of these paths will be collected,
and the test class will grow a method named ``test_jslint_filename.js``.

You can ignore JSLint error by setting ``ignore`` on the test class (a list of
substrings that are matched against each JSLint output line):

    ignore = (
        "Use a named parameter",
        )


Requirements
============

gocept.jslint is tested with Python 2.7, 3.6, 3.7 and 3.8.

gocept.jslint uses `node.js`_ to run jshint, so you need to have node.js
(version 0.3 or later) with the ``jshint`` npm module installed and the
``jshint`` binary available on your ``$PATH``.

You can customize the name of the jshint binary by setting ``jshint_command``
on the TestCase, or set the environment variable ``JSHINT_COMMAND``.

.. _node.js: http://nodejs.org/
