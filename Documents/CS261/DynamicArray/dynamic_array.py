# DynamicArray: An array that grows to accommodate new elements.
# Your implementation should pass the tests in test_dynamic_array.py.
# YOUR NAME
# import numpy
import numpy as np

DEFAULT_CAPACITY = 10
class DynamicArray:
    def __init__(self):
        
        self.capacity = DEFAULT_CAPACITY
        self.next_index = 0
        self.data = np.ndarray(self.capacity,dtype= object)
 

    
    def __len__(self):
        lenght= 0
        for object in self.data:
            if object !=None:
                lenght +=1
        return lenght

    def is_empty(self):
        if self.__len__() == 0: 
            return True
        else:
            return False
    def is_full(self) -> bool:
        return self.next_index >= self.capacity
    
    def __getitem__(self, index): 
        if index <= (self.next_index -1) and index >= 0:
            return self.data[index]
        else:
            raise IndexError('Out of Range')
    def append(self, value):
        self.next_index+=1
        if self.next_index > self.capacity:
            self.capacity *=2
        self.data[self.next_index - 1] = value
    def clear(self):
        new_array = np.full(self.capacity, None, dtype = object)
        self.data = new_array
        self.next_index = 0 
    def pop(self):
        if not self.next_index == 0:
            removed_value = self.data[self.next_index -1]
            self.data[self.next_index -1] = None
            self.next_index -= 1
            return removed_value
        else:
            raise IndexError("Can not pop from empty array")
    def delete(self, index):
        if index <= (self.next_index -1) and index >= 0:
            self.data[self.next_index - 1] = None
            self.next_index -= 1
            if self.next_index <= self.capacity // 2:
                self.capacity = (self.capacity // 2)
        else:
            raise IndexError("out of bounds")
    def insert(self, index, value):
        if index <= (self.next_index) and index >= 0:
            self.next_index += 1
            if self.next_index > self.capacity:
                 self.capacity *=2
            self.data[index] = value
        else:
            raise IndexError("out of bounds")

    def max(self):
        max_value = self.data[0]
        for x in np.nditer(self.data[1:self.next_index], flags=['refs_ok', 'zerosize_ok']):
            if x > max_value:
                max_value = x
        return max_value
    def min(self):
        min_value = self.data[0]
        for x in np.nditer(self.data[1:self.next_index], flags=['refs_ok', 'zerosize_ok']):
            if x < min_value:
                min_value = x
        return min_value
    def sum(self):
        total = self.data[0];
        for x in np.nditer(self.data[1:self.next_index], flags=['refs_ok', 'zerosize_ok']):
            total += x
        return total
        