import ctypes
import math

class DynamicArray:

    def __init__(self, start_capacity = 8, growth_t = "double"):
        self.capacity = start_capacity
        self.lenght = 0 
        self.data = (self.capacity * ctypes.py_object)()
        self.growth_type = growth_t
        self.resize_count = 0

    def append(self, value):
        if self.lenght == self.capacity:
            self.resize()

        self.data[self.lenght] = value
        self.lenght += 1

    def resize(self):
        if self.growth_type == "double":
            growth = 2

        elif self.growth_type == "fixed":
            growth = 1 + 4 / 10

        elif self.growth_type == "dynamic":
            growth = 1 + (4 / 10) / math.log2(self.lenght + 2)

        else:
            raise ValueError("unknown growth type")
        
        new_capacity = int(self.capacity * growth)
        if new_capacity <= self.capacity:
            new_capacity = self.capacity + 1

        new_data = (new_capacity * ctypes.py_object)()
        for i in range(self.lenght):
            new_data[i] = self.data[i]

        self.data = new_data
        self.capacity = new_capacity
        self.resize_count += 1

    def __getitem__(self, index):
        if index < 0 or index >= self.lenght:
            raise IndexError("index outside the array")
        return self.data[index]
    
    def __setitem__(self, index, value):
        if index < 0 or index >= self.lenght:
            raise IndexError("index outside the array")
        self.data[index] = value

    def __len__(self):
        return self.lenght
    
    def __iter__(self):
        for i in range(self.lenght):
            yield self.data[i]


arr = DynamicArray(start_capacity=8, growth_t="double")

for i in range(20):
    arr.append(i)

print("Lenght: ", len(arr))
print("capacity: ", arr.capacity)
print("overdrafts ", arr.resize_count)

print("arr[5] =", arr[5])
arr[5] = 69
print("arr[5] after change", arr[5])

for x in arr:
    print(x, end=" ")