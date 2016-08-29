#!/usr/bin/env python3
#
# Written by:
#   Maciej Kisielewski <kissiel@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import argparse
import os
import shutil
import sys


def main():
    types_db = build_types_db()
    parser = argparse.ArgumentParser()
    parser.epilog = 'Available types: {}'.format(
        ', '.join(sorted(types_db.keys())))
    parser.add_argument('FILE', help='Name of the file to generate')
    parser.add_argument('TYPE', help='Type of the file, e.g. "python"',
                        nargs='?')
    parser.add_argument('--force', '-f',
                        help='Force writing to FILE, even if target exists',
                        action='store_true')
    args = parser.parse_args()
    generate(args.FILE, args.TYPE, types_db, args.force)


def generate(filename, type, types_db, overwrite=False):
    if not type:
        print('Type not supplied... ', end='')
        ext = os.path.splitext(filename)[1]
        if not ext:
            print('and could not infer type')
            sys.exit(1)
        else:
            type = ext[1:]
            print('Type inferred: {}'.format(type))
    if type not in types_db:
        print('Unknown type: {}'.format(type))

    if os.path.exists(filename) and not overwrite:
        print('{} already exists. Use -f to overwrite'.format(filename))
        sys.exit(1)

    shutil.copy(types_db[type], filename)


def build_types_db():
    dirs = []
    if 'XDG_CONFIG_DIRS' in os.environ:
        dirs += [d for d in os.environ['XDG_CONFIG_DIRS'].split(':') if d]
    if 'XDG_CONFIG_HOME' in os.environ:
        dirs.append(os.environ['XDG_CONFIG_HOME'])
    elif 'HOME' in os.environ:
        dirs.append('$HOME/.config')
    dirs = [os.path.join(os.path.expandvars(d), 'bcg', 'types') for d in dirs]
    dirs.append(os.path.join(os.path.dirname(__file__), 'types'))
    types = dict()
    for d in dirs:
        if not os.path.isdir(d):
            continue
        for f in os.listdir(d):
            full_path = os.path.join(d, f)
            if os.path.isfile(full_path):
                types[f] = full_path
    return types

if __name__ == '__main__':
    main()
