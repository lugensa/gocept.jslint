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


class RunTest(unittest.TestCase):

    def test_runs_jslint(self):

        class Example(gocept.jslint.TestCase):
            include = ('gocept.jslint.tests:fixtures',)
            options = ()

        Example('test_jslint_one.js').run()
