import ctypes

class MeraList:
    def __init__(self):
        self.size = 1          # current capacity
        self.n = 0             # number of elements
        self.A = self.__make_array(self.size)

    def __len__(self):
        return self.n

    def __make_array(self, capacity):
        return (capacity * ctypes.py_object)()

    def __resize(self, new_capacity):
        B = self.__make_array(new_capacity)
        for i in range(self.n):
            B[i] = self.A[i]
        self.A = B
        self.size = new_capacity

    # Append
    def append(self, item):
        if self.n == self.size:
            self.__resize(2 * self.size)

        self.A[self.n] = item
        self.n += 1

    # Print
    def print_list(self):
        for i in range(self.n):
            print(self.A[i], end=" ")
        print()

    # Indexing
    def __getitem__(self, index):
        if not 0 <= index < self.n:
            raise IndexError("Index out of bounds")
        return self.A[index]

    # Pop
    def pop(self):
        if self.n == 0:
            raise IndexError("Pop from empty list")

        value = self.A[self.n - 1]
        self.A[self.n - 1] = None
        self.n -= 1
        return value

    # Clear
    def clear(self):
        self.n = 0
        self.size = 1
        self.A = self.__make_array(self.size)

    # Find
    def find(self, value):
        for i in range(self.n):
            if self.A[i] == value:
                return i
        return -1

    # Insert
    def insert(self, index, value):
        if not 0 <= index <= self.n:
            raise IndexError("Index out of bounds")

        if self.n == self.size:
            self.__resize(2 * self.size)

        for i in range(self.n, index, -1):
            self.A[i] = self.A[i - 1]

        self.A[index] = value
        self.n += 1

    # Delete by index
    def delete(self, index):
        if not 0 <= index < self.n:
            raise IndexError("Index out of bounds")

        for i in range(index, self.n - 1):
            self.A[i] = self.A[i + 1]

        self.A[self.n - 1] = None
        self.n -= 1

    # Remove by value
    def remove(self, value):
        index = self.find(value)
        if index == -1:
            raise ValueError("Value not found")
        self.delete(index)


# =========================
# Execution Starts Here
# =========================

if __name__ == "__main__":

    L = MeraList()

    # Append
    L.append(10)
    L.append(20)
    L.append(30)
    L.append("Hello")

    print("Initial List: - Dynamic_Array.py:112")
    L.print_list()

    # Length
    print("Length: - Dynamic_Array.py:116", len(L))

    # Indexing
    print("Element at index 2: - Dynamic_Array.py:119", L[2])

    # Insert
    L.insert(1, 15)
    print("After Insert at index 1: - Dynamic_Array.py:123")
    L.print_list()

    # Find
    print("Index of 20: - Dynamic_Array.py:127", L.find(20))

    # Delete
    L.delete(2)
    print("After Delete index 2: - Dynamic_Array.py:131")
    L.print_list()

    # Remove
    L.remove(15)
    print("After Remove 15: - Dynamic_Array.py:136")
    L.print_list()

    # Pop
    print("Popped Element: - Dynamic_Array.py:140", L.pop())
    L.print_list()

    # Clear
    L.clear()
    print("After Clear, Length: - Dynamic_Array.py:145", len(L))