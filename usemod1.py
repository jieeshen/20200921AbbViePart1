import sys
import os

# from folder.folder.folder read module.py
# from pkg.pkg.pkg import module
from abbvie.marketing import avutil

from utility.foo import bar
import utility.foo

bar()
utility.foo.bar()

# find abbvie/tech/data/avutil.py in PYTHONPATH and execute it

#  search folders in sys.path

avutil.spam()
avutil.toast()

for fruit in avutil.FRUITS:
    print(fruit)
print()

for path in sys.path:
    print(path)


# PYTHONPATH (WINDOWS)   dir1;dir2;dir3   just like PATH
# PYTHONPATH (non-WINDOWS)   dir1:dir2:dir3   just like PATH
print(sys.version_info)
print(sys.prefix)
print(sys.platform)  # win32 darwin linux

# print(dir(os))
