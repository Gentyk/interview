import inspect
import functools


def dec1(func):
    # декорирование функции без аргументов
    def wrapper():
        func()
        print("робит")

    return wrapper


def dec_with_args(func):
    # декорирование функции c аргументами
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        print("робит")

    return wrapper


def dec_class_def(func):
    # декорирование функции класса
    def wrapper(self, *args, **kwargs):
        func(self, *args, **kwargs)
        print("робит")

    return wrapper


def dec_with_docs(func):
    # с собеседование в тиньков
    # необходимо сохранить доку и сигнатуру(список параметров исходной функции)
    # решение https://sorokin.engineer/posts/ru/python_decorator_function_signature.html
    # https://stackoverflow.com/questions/23081829/why-python-decorator-will-lose-func-attribute-doc
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)

    wrapper.__signature__ = inspect.signature(func)
    return wrapper


# демонстрация применения
@dec1
def f1():
    print("f1 works")


@dec_with_args
def f2(msg):
    print("f2 works", msg)


class A:
    @dec_class_def
    def g(self, h=1):
        print("class A work", h * 5)


f1()
f2("fuck")
obj = A()
obj.g()


def nice_fiction(msg: str, test: bool = False):
    """Это описание функции"""
    print("f2 works", msg)


print(nice_fiction.__doc__)  # Это описание функции
print(inspect.signature(nice_fiction))  # (msg: str, test: bool = False)


@dec_with_args
def nice_fiction2(msg: str, test: bool = False):
    """Это описание функции"""
    print("f2 works", msg)


print(nice_fiction2.__doc__)  # None
print(inspect.signature(nice_fiction2))  # (*args, **kwargs)


@dec_with_docs
def nice_fiction3(msg: str, test: bool = False):
    """Это описание функции"""
    print("f2 works", msg)


print(nice_fiction3.__doc__)  # Это описание функции
print(inspect.signature(nice_fiction3))  # (msg: str, test: bool = False)
