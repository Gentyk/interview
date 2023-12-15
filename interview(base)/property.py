# Позволяет использовать функцию, как аттрибут класса
class Prop:
    def __init__(self, function):
        self.func = function

    def __get__(self, instance, owner):
        if not instance:
            return self
        return self.func(instance)


class A:
    @Prop
    def f(self):
        return "кошмар"


a = A()
print(a.f)
