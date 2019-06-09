# Если вы создадите класс с методом __call__ и создадите объект, у вас объект "превратится" в функцию.
class Name:
    def __call__(self, first, second):
        return first + second


f = Name()
print(f(1,2))
