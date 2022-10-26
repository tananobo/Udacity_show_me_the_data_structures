
import os
from collections import deque

def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    if not os.path.isdir(path):
        print("no such directory!")
        return
    found_files = []
    deque_dir_list = deque()
    deque_dir_list.append(path)
    while deque_dir_list:
        dir = deque_dir_list.popleft()
        for item in os.listdir(dir):
            if os.path.isfile(os.path.join(dir, item)) and item.endswith(suffix):
                found_files.append(os.path.join(dir, item))
            if os.path.isdir(os.path.join(dir, item)):
                deque_dir_list.append(os.path.join(dir, item))

    return found_files

# TEST directory environment
"""
./testdir
./testdir/subdir1
./testdir/subdir1/a.c
./testdir/subdir1/a.h
./testdir/subdir2
./testdir/subdir2/.gitkeep
./testdir/subdir3
./testdir/subdir3/subsubdir1
./testdir/subdir3/subsubdir1/b.c
./testdir/subdir3/subsubdir1/b.h
./testdir/subdir4
./testdir/subdir4/.gitkeep
./testdir/subdir5
./testdir/subdir5/a.c
./testdir/subdir5/a.h
./testdir/t1.c
./testdir/t1.h
"""

# TEST 1: Udacity provides: output should be ['./testdir/t1.c', './testdir/subdir5/a.c', './testdir/subdir1/a.c', './testdir/subdir3/subsubdir1/b.c']
print("======TEST1======: Udacity provides")
print(find_files(".c","."))


# TEST 2: another suffix: output should be ['./testdir/t1.h', './testdir/subdir5/a.h', './testdir/subdir1/a.h', './testdir/subdir3/subsubdir1/b.h']
print("======TEST2======: another suffix")
print(find_files(".h","."))

# TEST 3: directory change: ouput should be ['./testdir/subdir1/a.c']
print("======TEST3======: another directory")
print(find_files(".c","./testdir/subdir1"))

# TEST 4: no specifix suffix is defined: output should be ['./testdir/t1.c', './testdir/subdir5/a.c', './testdir/subdir1/a.c', './testdir/subdir3/subsubdir1/b.c''./testdir/t1.h', './testdir/subdir5/a.h', './testdir/subdir1/a.h', './testdir/subdir3/subsubdir1/b.h']
print("======TEST4======: no suffix (all files)")
print(find_files("","."))

# TEST 5: strenge suffix: output should be []
print("======TEST5======: strange suffix (all files)")
print(find_files("strange","."))

# TEST 5: strenge suffix: output should be message "no such directory!" and None
print("======TEST6======: no existance directory is pointed")
print(find_files("",""))