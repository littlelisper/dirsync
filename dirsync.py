#!/bin/python3

import os
import shutil
import sys

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
    
if (len(sys.argv) != 3):
    dir1_path = os.path.dirname(str(input("Directory 1: ")))
    dir2_path = os.path.dirname(str(input("Directory 2: ")))
else:
    dir1_path = os.path.dirname(sys.argv[1])
    dir2_path = os.path.dirname(sys.argv[2])

sync(dir1_path, dir2_path)
