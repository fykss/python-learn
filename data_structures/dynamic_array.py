# Implementation of Dynamic Array. DYNAMIC ARRAY CLASS (Similar to Python List)
# https://www.geeksforgeeks.org/implementation-of-dynamic-array-in-python/


import ctypes


class DynamicArray(object):
    def __init__(self):
        self.n = 0  # Count actual elements (Default is 0)
        self.capacity = 1  # Default Capacity
        self.A = self.make_array(self.capacity)

    def len(self):
        """ 
        Return number of elements sorted in array 
        """
        return self.n

    def get(self, index):
        """ 
        Return element at index 
        """
        if not 0 <= index < self.n:
            return IndexError("Index is out of bounds !")

        return self.A[index]

    def append(self, item):
        """ 
        Add element to end of the array 
        """
        if self.n == self.capacity:
            self.capacity *= 2
        self.A[self.n] = item  # Set self.n index to element
        self.n += 1

    def make_array(self, new_cap):
        return (new_cap * ctypes.py_object)()


dynamic_array = DynamicArray()
print(dynamic_array.len())

dynamic_array.append(1)
print(dynamic_array.len())

print(dynamic_array.get(0))
print(dynamic_array.get(1))

