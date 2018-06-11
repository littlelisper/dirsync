#!/bin/python3

import os
import hashlib
import sys
import shutil

#change of plans, you are currently unassigned
def sha1sum(path):
    hash = hashlib.sha1()
    file = open(path, "rb")
    bytes = file.read()
    hash.update(bytes)
    return hash.hexdigest()

 
def lsrec(dir_path): 
    result = []
    elements = os.listdir(dir_path)
    for elem in elements:
        path = os.path.join(dir_path, elem)
        if (os.path.isdir(path)):
            result.extend(lsrec(path))
        else:
            result.append(path)
    return result

parent = lambda x: os.path.dirname(x)
base = lambda x: os.path.basename(x)

def recmkdir(path, left = []):
    if (os.path.exists(path)):
        if (len(left) == 0):
            return
        else:
            os.makedirs(os.path.join(path, left[0]))
            recmkdir(os.path.join(path, left[0]), left[1:])
    else:
        left.insert(0, base(path))
        recmkdir(parent(path), left)

def handlecopy(apath, bpath):
    atime = os.path.getmtime(apath)
    btime = os.path.getmtime(bpath)
    if (atime > btime):
        shutil.copy2(apath, bpath)
    else:
        shutil.copy2(bpath, apath)
        
def sync(dir1, dir2, dir_elems):
    for elem in dir_elems:
        dir1_eq = os.path.join(dir1, elem)
        dir2_eq = os.path.join(dir2, elem)
        if (os.path.exists(dir2_eq)):
            handlecopy(dir1_eq, dir2_eq)
            continue
        else:
            recmkdir(parent(dir2_eq))
            shutil.copy2(dir1_eq, dir2_eq)
        
def dirextract(dir, elems):
    dirlen = len(dir)
    return [elem[dirlen + 1:] for elem in elems]

def supersync(dir1, dir2):
    dir1_elems = lsrec(dir1)
    dir2_elems = lsrec(dir2)
    sync(dir1, dir2, dirextract(dir1, dir1_elems))
    sync(dir2, dir1, dirextract(dir2, dir2_elems))

supersync(sys.argv[1], sys.argv[2])
