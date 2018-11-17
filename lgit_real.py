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
    content_index = []
    command = args.command[0]
    if command == 'init':
        create_dir()
    elif command == 'add':
        argument = args.command[1:]
        flag = 1
        for item in argument:
            if not os.path.exists(item):
                print("fatal: pathspec '" + item +
                      "'did not match any files")
                flag = 0
                break
        if flaf == 1:
            for item in argument:
                list_index = lgit_add(item)
                content_index = add_list(list_index, content_index)  # (3)
            write_index('\n'.join(content_index) + '\n')  # (1)


def write_index(content):  #write file index # (1)
    path = os.getcwd()
    with open(path + "/.lgit/index", 'a+') as f_index:
        f_index.write(content)
    f_index.close()



#-------------------------------LGIT ADD----------------------------------
def lgit_add(file_name):
    list_index = []
    if os.path.isdir(file_name):
        files = directory_tree_list(file_name)
        for file in files:
            index = create_file_objects(file)
            list_index.append(index)
            print(index)
    if os.path.isfile(file_name):
        index = create_file_objects(file_name)
        print(index)
        list_index.append(index)
    return list_index


def directory_tree_list(path):
    list_file = []
    for dirname, dirnames, filenames in os.walk(path):
        for filename in filenames:
            list_file.append(os.path.join(dirname, filename))
    return list_file


def create_file_objects(filename):
    path = os.getcwd()
    file_content = open(filename,'r').read()
    path_objects = path +'/.lgit/objects'
    hash_sha1 = caculate_sha1_file(filename)
    file_name = hash_sha1[2:]
    dir_name =  hash_sha1[:2]
    if not os.path.exists(path_objects + "/" + dir_name):
        os.mkdir(path_objects + "/" + dir_name)
    file = open(path_objects + "/" + dir_name + "/" + file_name, 'w+')
    file.write(file_content)
    file.close()
    hash_sha2 = caculate_sha1_file(path_objects + "/" + dir_name + "/" + file_name)
    index = create_structure_index(filename, hash_sha1, hash_sha2)
    return(index)


def caculate_sha1_file(filename):
    hasher = hashlib.sha1()
    with open(filename, 'rb') as afile:
        buf = afile.read()
        while len(buf) > 0:
            hasher.update(buf)
            buf = afile.read()
    return hasher.hexdigest()


def create_structure_index(filename, hash1, hash2):
    file_index = []
    timestamp = str(get_timestamp(filename))
    file_index.append(timestamp)
    file_index.append(hash1)
    file_index.append(hash2)
    #SHA1 of the file content after commited
    file_index.append(' ' * 40)
    file_index.append(filename)
    return ' '.join(file_index)


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


#--------------------------------INIT---------------------------------
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


if __name__ == '__main__':
    main()
