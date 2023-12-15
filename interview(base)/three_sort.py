from random import randint


class Tree:
    def __init__(self, parent, value):
        self.parent = parent
        self.value = value
        self.left = None
        self.right = None

    def set_left(self, value):
        self.left = Tree(self, value)

    def set_right(self, value):
        self.right = Tree(self, value)

    def set(self, value):
        if value >= self.value:
            if self.right:
                self.right.set(value)
            else:
                self.set_right(value)
        else:
            if self.left:
                self.left.set(value)
            else:
                self.set_left(value)

    def get(self):
        return_array = []
        if self.left:
            left = self.left.get()
            if isinstance(left, int):
                return_array.append(left)
            else:
                return_array.extend(left)
        return_array.append(self.value)
        if self.right:
            right = self.right.get()
            if isinstance(right, int):
                return_array.append(right)
            else:
                return_array.extend(right)
        return return_array


def mass_to_three(array):
    three = None
    for val in array:
        if not three:
            three = Tree(None, val)
        else:
            three.set(val)
    return three


array = [randint(1, 900) for i in range(9)]
three = mass_to_three(array)
print(three.get())
