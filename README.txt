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

        include = ['my.package.browser:js',
                   'my.package.browser:js/lib']

``include`` is a list of paths, either absolute filesystem paths or "resource
paths" of the form ``packagename:path``, that are passed to pkg_resources.

All files ending in ``.js`` contained in each of these paths will be collected,
and the test class will grow a method named ``test_jslint_filename.js``.


Requirements
============

gocept.jslint uses `node.js`_ to run jslint (powered by the `jslint-reporter`_
wrapper for the original JSLint script), so you need to have node.js installed
and the ``node`` binary available on your ``$PATH``.


.. _node.js: http://nodejs.org/
.. _jslint-reporter: https://github.com/FND/jslint-reporter/
