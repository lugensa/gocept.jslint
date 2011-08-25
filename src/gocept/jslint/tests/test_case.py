# Copyright (c) 2011 gocept gmbh & co. kg
# See also LICENSE.txt

import gocept.jslint
import sys

if sys.version_info < (2, 7):
    import unittest2 as unittest
else:
    import unittest


class CollectFilesTest(unittest.TestCase):

    def test_generates_method_for_each_js_file(self):

        class Example(gocept.jslint.TestCase):
            include = ('gocept.jslint.tests:fixtures',)

        self.assertTrue(hasattr(Example, 'test_jslint_one.js'))
        self.assertTrue(hasattr(Example, 'test_jslint_two.js'))

    def test_same_filename_in_multiple_directories_appends_number(self):

        class Example(gocept.jslint.TestCase):
            include = ('gocept.jslint.tests:fixtures',
                       'gocept.jslint.tests:fixtures/second')

        self.assertTrue(hasattr(Example, 'test_jslint_one.js'))
        self.assertTrue(hasattr(Example, 'test_jslint_two.js'))
        self.assertTrue(hasattr(Example, 'test_jslint_one.js_1'))

    def test_excluded_filenames_do_not_get_method(self):

        class Example(gocept.jslint.TestCase):
            include = ('gocept.jslint.tests:fixtures',)
            exclude = ('two.js',)

        self.assertTrue(hasattr(Example, 'test_jslint_one.js'))
        self.assertFalse(hasattr(Example, 'test_jslint_two.js'))


class RunTest(unittest.TestCase):

    def test_jslint_error_should_fail_test(self):

        class Example(gocept.jslint.TestCase):
            include = ('gocept.jslint.tests:fixtures',)
            options = ()

        result = unittest.TestResult()
        Example('test_jslint_one.js').run(result)
        self.assertEqual(1, len(result.failures))
        traceback = result.failures[0][1]
        self.assertTrue(
            "one.js:2:5:Missing 'use strict' statement" in traceback)

    def test_no_jslint_error_should_pass_test(self):

        class Example(gocept.jslint.TestCase):
            include = ('gocept.jslint.tests:fixtures',)
            options = ('--sloppy',)

        result = unittest.TestResult()
        Example('test_jslint_one.js').run(result)
        self.assertEqual(0, len(result.failures))

    def test_ignored_errors_should_pass_test(self):

        class Example(gocept.jslint.TestCase):
            include = ('gocept.jslint.tests:fixtures',)
            options = ()
            ignore = ("Missing 'use strict' statement")

        result = unittest.TestResult()
        Example('test_jslint_one.js').run(result)
        self.assertEqual(0, len(result.failures))

    def test_nodejs_not_available_should_skip(self):

        class Example(gocept.jslint.TestCase):
            node_js_command = 'doesnotexist'
            include = ('gocept.jslint.tests:fixtures',)

        result = unittest.TestResult()
        Example('test_jslint_one.js').run(result)
        self.assertEqual(1, len(result.skipped))
