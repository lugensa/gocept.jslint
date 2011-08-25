# Copyright (c) 2011 gocept gmbh & co. kg
# See also LICENSE.txt

import os


def which(program):
    # adapted from <http://stackoverflow.com/questions/377017>
    path, name = os.path.split(program)
    for path in ['.'] + os.environ['PATH'].split(os.pathsep):
        filename = os.path.join(path, program)
        if os.path.exists(filename) and os.access(filename, os.X_OK):
            return filename
