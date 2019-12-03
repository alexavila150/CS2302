class Person(object):
    age = None

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return repr((self.name, self.age))


p1 = Person("Alex", 19)
p2 = Person("Eddie", 20)
p3 = Person("Matthew", 19)
p4 = Person("Esteban", 20)

list1 = [p3, p2, p1, p4]
print(list1)
list1 = sorted(list1, key=lambda person: person.age)
print(list1)
