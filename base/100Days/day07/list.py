import os
import time


def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
        yield a


if __name__ == '__main__':
    list1 = [1, 3, 5, 7, 100]
    print(list1)
    list2 = ['hello'] * 3
    print(list2)
    print(list1[-1])
    for index in range(len(list1)):
        print(list1[index])
    for elem in list1:
        print(elem)
    for index, elem in enumerate(list1):
        print(index, elem)
    list1.append(200)
    list1.insert(1, 400)
    list1.extend([1000, 2000])
    print(list1)
    list1.pop(0)
    list1.pop(len(list1) - 1)
    print(list1)
    print(sorted(list1))
    print(sorted(list1, reverse=True))

    f = [x + y for x in 'ABCDE' for y in '1234567']
    print(f)

    # for val in fib(20):
    #     print(val)

    t = ('小天', 38, True, '上海')
    print(t)

    list3 = list(t)
    list3[0] = '哈哈哈'
    t1 = tuple(list3)
    print(t1)

    set1 = {1, 2, 3, 3, 3, 2, 0}
    set2 = set(range(1, 10))
    set3 = set((1, 2, 3, 3, 2, 1))
    print(set2, set3)

    set2.add(4)
    set2.add(10)
    set2.update([11, 12])
    print(set2)

    print(set1 & set2)
    print(set1.intersection(set2))
    print(set1 | set2)
    print(set1.union(set2))
    print(set2 - set1)
    print(set1.difference(set2))
    print(set1 ^ set2)

    scores = {'小明': 95, '小白': 78, '小黑': 82}
    print(scores)
    items1 = dict(one=1, two=2, three=3, four=4)
    items2 = dict(zip(['a', 'b', 'c'], '123'))
    items3 = {num: num ** 2 for num in range(1, 10)}
    print(items1, items2, items3)
    print(scores.get('小明1', 60))
    # scores.popitem()
    print(scores.pop('小明2', 100))
    print(scores)

    # content = '北京欢迎你为你开天辟地…………'
    # while True:
    #     # 清理屏幕上的输出
    #     os.system('cls')  # os.system('clear')
    #     print(content)
    #     # 休眠200毫秒
    #     time.sleep(0.2)
    #     content = content[1:] + content[0]

