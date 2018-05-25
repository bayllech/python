import os

import time

# f = open("for.py")
# print(f)
# for line in f:
#     print(line)

with open("for.py") as f:
    print(f.read())

file_stat = os.stat("for.py")
print(file_stat)
print(time.localtime(file_stat.st_ctime))