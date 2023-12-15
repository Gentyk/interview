def singleton1(class_):
    instance = {}

    def wrapper(*args, **kwargs):
        if class_ not in instance:
            instance[class_] = class_(*args, **kwargs)
        return instance[class_]

    return wrapper


class Singleton2(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton2, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


@singleton1
class A:
    pass


class B(metaclass=Singleton2):
    pass


obj1 = A()
obj2 = A()
print(obj1, obj2)


obj1 = B()
obj2 = B()
print(obj1, obj2)
