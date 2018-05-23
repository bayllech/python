# a = [1,2,3]
# b = ["11","12","13"]
# d = []
# for x,y in zip(a,b):
#     d.append(str(x) + ":" + y)
# print(d)

# a = [1,2,3]
# b = [11,12,13]
# d = []
# for x,y in zip(a,b):
#     d.append(str(x) + "," + str(y))
# print(d)
from math import sqrt

myinfor={"name":"qiwsir","site":"qiwsir.github.io","lang":"python"}
info = dict(zip(myinfor.values(),myinfor.keys()))
print(info)

seasons = ['Spring', 'Summer', 'Fall', 'Winter']
print(list(enumerate(seasons,start=1)))


for n in range(99,1,-1):
    root = sqrt(n)
    if root == int(root):
        print(n)
        break
    else:
        print("nothing.")
