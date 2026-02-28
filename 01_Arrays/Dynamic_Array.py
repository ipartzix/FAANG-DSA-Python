import ctypes

class MeraList:
    def __init__(self):
        self.size = 1
        self.n = 0
        self.A = self.__make_array(self.size)

    def __len__(self):
        return self.n

    def append(self, item):
        if self.n == self.size:
            self.__resize(2 * self.size)

        self.A[self.n] = item
        self.n += 1

    def __resize(self, new_capacity):
        B = self.__make_array(new_capacity)

        for i in range(self.n):
            B[i] = self.A[i]

        self.A = B
        self.size = new_capacity

    def __getitem__(self, index):
        if not 0 <= index < self.n:
            raise IndexError("Index out of bounds")

        return self.A[index]

    def __make_array(self, capacity):
        return (capacity * ctypes.py_object)()

    #  Print
    def print_list(self):
        for i in range(self.n):
            print(self.A[i], end=" ")
        print()

    #  Pop (remove last element)
    def pop(self):
        if self.n == 0:
            raise IndexError("Pop from empty list")

        value = self.A[self.n - 1]
        self.A[self.n - 1] = None
        self.n -= 1
        return value

    #  Clear
    def clear(self):
        self.n = 0
        self.size = 1
        self.A = self.__make_array(self.size)

    #  Find (return index)
    def find(self, value):
        for i in range(self.n):
            if self.A[i] == value:
                return i
        return -1

    #  Insert at index
    def insert(self, index, value):
        if not 0 <= index <= self.n:
            raise IndexError("Index out of bounds")

        if self.n == self.size:
            self.__resize(2 * self.size)

        for i in range(self.n, index, -1):
            self.A[i] = self.A[i - 1]

        self.A[index] = value
        self.n += 1

    #  Delete by index
    def delete(self, index):
        if not 0 <= index < self.n:
            raise IndexError("Index out of bounds")

        for i in range(index, self.n - 1):
            self.A[i] = self.A[i + 1]

        self.A[self.n - 1] = None
        self.n -= 1

    #  Remove by value
    def remove(self, value):
        index = self.find(value)

        if index == -1:
            raise ValueError("Value not found")

        self.delete(index)