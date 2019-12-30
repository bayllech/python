class Person(object):

    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self.name

    @property
    def age(self):
        return self.age

    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        if self._age <= 16:
            print('%s正在看动画片.' % self._name)
        else:
            print('%s正在斗地主.' % self._name)


def main():
    person = Person('大锤', 12)
    person.play()
    person.age = 22
    person.play()


if __name__ == '__main__':
    main()