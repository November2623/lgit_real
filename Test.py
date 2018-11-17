#!/usr/bin/env python3
import hashlib
import argparse
import os
from stat import *
import datetime

def get_argument():
    parser = argparse.ArgumentParser()
    parser.add_argument('command', nargs='+', help='init/add/commit/snapshots/index/config/status')
    args = parser.parse_args()
    return args.command


def caculate_sha1_file(filename):
    hasher = hashlib.sha1()
    with open(filename, 'rb') as afile:
        buf = afile.read()
        while len(buf) > 0:
            hasher.update(buf)
            buf = afile.read()
    return hasher.hexdigest()
def get_timestamp(filename):
    t = os.path.getmtime(filename)
    time = str(datetime.datetime.fromtimestamp(t))
    list1 = time.split('.')
    time = list1[0]
    list_time = list(time)
    timestamp = []
    for i in list_time:
        if i != '-' and i != ':' and i != ' ':
            timestamp.append(i)
    return(''.join(timestamp))

def directory_tree_list(path):
    for dirname, dirnames, filenames in os.walk(path):
        for filename in filenames:
            print(os.path.join(dirname, filename))
def get_timestamp(filename):
    stat = os.stat(filename)
    print(stat.st_mtime)
path = os.getcwd()
time('text.txt')
