#!/bin/python3

import os
import shutil
import argparse

def ls(dir_path, files = [], dirs = []): 
    elements = os.listdir(dir_path)
    for elem in elements:
        path = os.path.join(dir_path, elem)
        if (os.path.isdir(path)):
            dirs.append(path)
            files, dirs = ls(path, files, dirs)
        else:
            files.append(path)
    return files, dirs

def snip_path(dir_path, paths):
    length = len(dir_path)
    return [path[length+1:] for path in paths]

def dirs_sync(parent, dirs):
    for dir_path in dirs:
        path = os.path.join(parent, dir_path)
        if not (os.path.exists(path)):
            os.makedirs(path)

def files_sync(dir1_path, dir2_path, files):
    for file_path in files:
        source = os.path.join(dir1_path, file_path)
        destination = os.path.join(dir2_path, file_path)
        if not (os.path.exists(destination)):
            shutil.copy2(source, destination)
        else:
            stime = os.path.getmtime(source)
            dtime = os.path.getmtime(destination)
            if (stime > dtime):
                shutil.copy2(source, destination)

def sync(dir1_path, dir2_path):
    dir1_files, dir1_dirs = ls(dir1_path, [], [])
    dir2_files, dir2_dirs = ls(dir2_path, [], [])
    
    dir1_files = snip_path(dir1_path, dir1_files)
    dir1_dirs = snip_path(dir1_path, dir1_dirs)
    
    dir2_files = snip_path(dir2_path, dir2_files)
    dir2_dirs = snip_path(dir2_path, dir2_dirs)
    
    dirs_sync(dir2_path, dir1_dirs)
    files_sync(dir1_path, dir2_path, dir1_files)
    
    dirs_sync(dir1_path, dir2_dirs)
    files_sync(dir2_path, dir1_path, dir2_files)

def extract_paths(paths_file_stream):
    paths = paths_file_stream.read().splitlines()
    for i in range(0, len(paths), 2):
        sync(paths[i], paths[i+1])

parser = argparse.ArgumentParser(description='Asynchronous files sync among between directories')
parser.add_argument('-f', '--filename', type = argparse.FileType('r'), help='Read paths from a file')
parser.add_argument('-p', '--paths', help='Paths to sync', nargs=2)
args = parser.parse_args()

if (args.filename):
    extract_paths(args.filename)
elif (args.paths):
    sync(args.paths[0], args.paths[1])
else:
    if(input("Get paths from file? y/n: ") == 'y'):
        path_source = open(str(input("File path: ")), 'r')
        extract_paths(path_source)
    else:
        dir1_path = str(input("Dir1 path: "))
        dir2_path = str(input("Dir2 path: "))
        sync(dir1_path, dir2_path)
