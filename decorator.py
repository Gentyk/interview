def dec1(func):
    # декорирование функции без аргументов
    def wrapper():
        func()
        print("робит")
    return wrapper

def dec_with_args(func):
    # декорирование функции без аргументов
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        print("робит")
    return wrapper

def dec_class_def(func):
    # декорирование функции без аргументов
    def wrapper(self, *args, **kwargs):
        func(self, *args, **kwargs)
        print("робит")
    return wrapper

# демонстрация применения
@dec1
def f1():
    print('f1 works')

@dec_with_args
def f2(msg):
    print('f2 works', msg)


class A:

    @dec_class_def
    def g(self, h=1):
        print('class A work', h*5)

f1()
f2("fuck")
obj = A()
obj.g()