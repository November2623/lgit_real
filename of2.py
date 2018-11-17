#!/usr/bin/env python3
import argparse
import os
import hashlib
import shutil
import datetime

def get_argument():
    parser = argparse.ArgumentParser()
    parser.add_argument('command', nargs='+', help='init/add/commit/snapshots/index/config/status')
    parser.add_argument('--author', action='store')
    args = parser.parse_args()
    return args
def main():
    args = get_argument()
    command = args.command[0]
    if command == 'init':
        create_dir()
    elif command == 'add':
        argument = args.command[1:]
        for item in argument:
            if not os.path.exists(item):
                print("fatal: pathspec '" + item +
                      "'did not match any files")
                flag = 0
                break
            else:
                list_index = lgit_add(item)


def create_dir():
    path = os.getcwd() + '/.lgit'
    if os.path.exists(path):
        print('Reinitialized existing Git repository in ' + path)
        shutil.rmtree(path)
    else:
        print('Initialized empty Git repository in ' + path)
    os.mkdir(path)
    os.mkdir(path + '/commits')
    os.mkdir(path + '/objects')
    os.mkdir(path + '/snapshot')
    filename_index = os.path.join(path,'index')
    file = open(filename_index, 'w+')
    file.close()
    filename_config = os.path.join(path,'config')
    file = open(filename_config, 'w+')
    file.write(os.environ['LOGNAME'])
    file.close()
