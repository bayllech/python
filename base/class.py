class Foo(object):
    x = 1


foo = Foo()

Foo.x = 2
foo.x = 3
print(Foo.x)
print(foo.x)

__metaclass__ = type


# class Person:
#     def __init__(self, name):
#         self.name = name
#
#     def getName(self):
#         return self.name
#
#     def breast(self,n):
#         self.breast = n
#
#     def color(self,color):
#         print("%s is %s" % (self.name, color))
#
#     def how(self):
#         print("%s breast is %s" %(self.name, self.breast))
#
#
# girl = Person("canglaoshi")
# girl.breast(90)
#
# girl.color("white")
# girl.how()


class Person:
    def speak(self):
        print("I love you.")

    def setHeight(self):
        print("The height is: 1.60m.")

    def breast(self, n):
        print("My breast is: ",n)


class Girl(Person):
    def setHeight(self):
        print("The height is:1.70m .")


if __name__ == "__main__":
    cang = Girl()
    cang.setHeight()
    cang.speak()
    cang.breast(90)
