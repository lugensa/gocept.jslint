# Copyright (c) 2011 gocept gmbh & co. kg
# See also LICENSE.txt

import gocept.jslint
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
