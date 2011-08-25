=============
gocept.jslint
=============

This package integrates Douglas Crockford's JSLint tool (https://jslint.com)
with Python's unittest module.

It provides a special JSLint-TestCase class that collects JavaScript files (in
a configurable manner) and dynamically generates a test method for each file
that calls jslint on that file.

To use it, create a test class like this::

    class MyJSLintTest(gocept.jslint.TestCase):

        include = ('my.package.browser:js',
                   'my.package.browser:js/lib')
        options = (gocept.jslint.TestCase.options +
                   ('--predef=jQuery',))


``include`` is a list of "resource paths" of the form ``packagename:path``
(passed to pkg_resources).

``options`` is a list of arguments that are passed to JSLint (see its
`documentation`_ for details). The default value is::

    options = (
        '--browser',
        '--continue',
        '--newcap',
        '--nomen',
        '--sloppy',
        '--sub',
        '--unparam',
        '--vars',
        '--white',
        )

.. _documentation: http://www.jslint.com/lint.html#options

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

gocept.jslint requires Python 2.6 or later, but is not sure to run under Python
3.

gocept.jslint uses `node.js`_ to run jslint (powered by the `jslint-reporter`_
wrapper for the original JSLint script), so you need to have node.js (version
0.3 or later) installed and the ``node`` binary available on your ``$PATH``.

You can customize the name of the node.js binary by setting ``node_js_command``
on the TestCase.

gocept.jslint also provides a command-line script to run jslint, for
convenience. There you can customize the name of the node binary by setting the
environment variable ``NODE_JS_COMMAND``.


.. _node.js: http://nodejs.org/
.. _jslint-reporter: https://github.com/FND/jslint-reporter/
