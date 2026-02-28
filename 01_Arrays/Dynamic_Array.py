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
            # Resize when full
            self.__resize(2 * self.size)
        self.A[self.n] = item
        self.n += 1
    
    def __resize(self, new_capacity):
        B = self.__make_array(new_capacity)
        # Copy old elements
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

# Usage
L = MeraList()
L.append(10)
L.append(20)
L.append(30)
print(len(L))   # Output: 3
L.append("Hello")
print(len(L))   # Output: 4
print(L[3])     # Output: Hello
