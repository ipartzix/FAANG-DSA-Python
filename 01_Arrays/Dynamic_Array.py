import ctypes
class MeraList:
    def __init__(self):
        self.size = 1
        self.n = 0
        # create a C type array with size = self.size 
        self.A = self.__make_array(self.size) # pyright: ignore[reportAttributeAccessIssue]
    
    def __make_array(self,capacity):
        # this code create a c type array with fixed capacity also it is a referential array 
        return (capacity*ctypes.py_object)()
    
L = MeraList()
print(type(L))