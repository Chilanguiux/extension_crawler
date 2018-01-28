#! /usr/bin/env python
# -*- coding: utf-8 -*-
import os


def main():
    l = int()
    path = raw_input('Path: ')
    while not path:
        path = raw_input('Path: ')
    if not path or not os.path.exists(path):
        print 'please insert a proper path and try again'
    else:
        ext = raw_input('Extension: ')
        _newlist = []
        while not ext:
            ext = raw_input('Extension: ')
        files = [f for f in os.listdir(path) if f.endswith(ext)]
        for names in files:
            if names.endswith(ext):
                _newlist.append(names)
            else:
                print 'nothing found'
                continue
        for _datos in sorted(_newlist):
            l += 1
            print '{}.-'.format(l), _datos
        print 'number of files found: {}'.format(len(_newlist))


if __name__ == '__main__':
    main()
