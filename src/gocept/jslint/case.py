# Copyright (c) 2011 gocept gmbh & co. kg
# See also LICENSE.txt

import gocept.jslint.util
import json
import os.path
import pkg_resources
import re
import six
import subprocess
import sys
import tempfile

if sys.version_info < (2, 7):
    import unittest2 as unittest
else:
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
        name = cls._uniquify_name(dict, name)
        dict[name] = lambda x: x._run_jslint(filename)

    @classmethod
    def _uniquify_name(cls, dict, name):
        if name not in dict:
            return name
        base = name
        counter = 1
        while name in dict:
            name = '%s_%s' % (base, counter)
            if name not in dict:
                return name
            counter += 1

    @classmethod
    def _collect_files(cls, include, exclude):
        files = []
        for path in include:
            package, path = path.split(':', 1)
            for filename in pkg_resources.resource_listdir(package, path):
                basename, extension = os.path.splitext(filename)
                if extension.lower() != '.js':
                    continue
                files.append(pkg_resources.resource_filename(
                        package, os.path.join(path, filename)))

        result = []
        for path in files:
            basename = os.path.basename(path)
            if basename not in exclude:
                result.append(path)
        return result


class TestCase(six.with_metaclass(JSLintTestGenerator, unittest.TestCase)):

    jshint_command = os.environ.get('JSHINT_COMMAND', 'jshint')

    include = ()
    exclude = ()
    options = ()
    predefined = ()
    ignore = ()

    _error_summary = re.compile(r'^\d+ errors?$')

    def __init__(self, *args, **kw):
        super(TestCase, self).__init__(*args, **kw)
        self.jshint_present = gocept.jslint.util.which(self.jshint_command)

    def _run_jslint(self, filename):
        if not self.jshint_present:
            raise unittest.SkipTest(
                '%r not found on $PATH' % self.jshint_command)
        config = self._write_config_file()
        job = subprocess.Popen(
            [self.jshint_command, filename, '--config', config],
            stdout=subprocess.PIPE)
        job.wait()
        output, error = job.communicate()
        output = self._filter_ignored_errors(output)
        if output:
            self.fail('JSLint %s:\n%s' % (filename, output))

    def _write_config_file(self):
        settings = {}
        for option in self.options:
            settings[option] = True
        predefined = settings['predef'] = []
        for name in self.predefined:
            predefined.append(name)

        handle, filename = tempfile.mkstemp()
        output = open(filename, 'w')
        json.dump(settings, output)
        output.close()

        return filename

    def _filter_ignored_errors(self, output):
        result = []
        for line in output.splitlines():
            if self._error_summary.search(line.decode('utf-8')):
                continue
            ignore = False
            for pattern in self.ignore:
                if pattern in line:
                    ignore = True
                    break
            if ignore:
                continue
            result.append(line.decode('utf-8'))
        return '\n'.join(result)
