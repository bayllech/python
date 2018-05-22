from builtins import print, range

s = "abc"
print(s)

t = 123,'abc',["come","here"]
print(t)

person = {'name2':'qiwsir','name':'qiwsir','language':'python','site':'qiwsir.github.io'}
print(person)

for i in "world":
    print(i)

a_dict = {"name": "qiwsir", "lang": "python", "email": "qiwsir@gmail.com", "website": "www.itdiffer.com"}

for i in a_dict:
    print(i, "--->>>", a_dict[i])

# for k,v in a_dict.iteritems():  python3 已废除 只保留items()
#     print(k,v)