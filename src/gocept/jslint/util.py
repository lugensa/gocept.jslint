# Copyright (c) 2011 gocept gmbh & co. kg
# See also LICENSE.txt

import os
import pkg_resources
import subprocess
import sys


def which(program):
    # adapted from <http://stackoverflow.com/questions/377017>
    path, name = os.path.split(program)
    for path in ['.'] + os.environ['PATH'].split(os.pathsep):
        filename = os.path.join(path, program)
        if os.path.exists(filename) and os.access(filename, os.X_OK):
            return filename


def run_jslint():
    jslint = pkg_resources.resource_filename(
        'gocept.jslint.js', 'node-jslint.js')
    node_js_command = os.environ.get('NODE_JS_COMMAND', 'node')
    subprocess.call([node_js_command, jslint] + sys.argv[1:])
