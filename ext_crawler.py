#! /usr/bin/env python
# -*- coding: utf-8 -*-
import os
import logging


def path_from_user():
    path = None
    while not path:
        path = raw_input('Path: ')
        if not os.path.exists(path):
            print 'path do not exists!'
            exit(0)
        else:
            return path

def ext_from_user():
    ext = None
    _newlist = []
    path = path_from_user()
    l = int()
    while not ext or _newlist is None:
        ext = raw_input('Extension: ')
    files = [f for f in os.listdir(path) if f.endswith(ext)]
    if not files:
        print ('extension cant be found: {}'.format(ext))
        return
    _newlist.append(files)
    for datos in sorted(_newlist):
        for _files in datos:
            l += 1
            print ('{}.-'.format(l) + _files)
        print ('number of files found: {}'.format(len(datos)))


def main():
    ext_from_user()


if __name__ == '__main__':
    main()
