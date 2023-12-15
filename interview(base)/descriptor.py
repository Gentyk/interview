class Deskr:
    def __init__(self, value):
        self.value = value

    def __get__(self, instance, objtype):
        print("get value")
        if self.value:
            return self.value
        else:
            return None

    def __set__(self, instance, value):
        print("set value")
        self.value = value


class A:
    a = Deskr(12)


b = A()
b.a = 20
print(b.a)
