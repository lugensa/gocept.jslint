# Copyright (c) 2011 gocept gmbh & co. kg
# See also LICENSE.txt

import glob
import os.path
import pkg_resources
import subprocess
import unittest


class JSLintTestGenerator(type):

    def __new__(cls, name, bases, dict):
        for filename in cls._collect_files(
            dict.get('include', ()), dict.get('exclude', ())):
            cls._create_jslint_runner(dict, filename)
        return type.__new__(cls, name, bases, dict)

    @classmethod
    def _create_jslint_runner(cls, dict, filename):
        name = 'test_jslint_%s' % os.path.basename(filename)
        if name in dict:
            name += '_1'
        dict[name] = lambda x: x._run_jslint(filename)

    @classmethod
    def _collect_files(cls, include, exclude):
        paths = []
        for path in include:
            package, path = path.split(':', 1)
            paths.append(pkg_resources.resource_filename(package, path))

        files = []
        for path in paths:
            files.extend(glob.glob(os.path.join(path, '*.js')))

        result = []
        for path in files:
            basename = os.path.basename(path)
            if basename not in exclude:
                result.append(path)
        return result


class TestCase(unittest.TestCase):

    __metaclass__ = JSLintTestGenerator

    include = ()
    exclude = ()
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

    def _run_jslint(self, filename):
        jslint = pkg_resources.resource_filename(
            'gocept.jslint.js', 'node-jslint.js')
        job = subprocess.Popen(
            ['node', jslint] + list(self.options) + [filename],
            stdout=subprocess.PIPE)
        status = job.wait()
        output, error = job.communicate()
        if status != 0:
            self.fail('JSLint %s:\n%s' % (filename, output))
