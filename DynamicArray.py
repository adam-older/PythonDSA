import ctypes

class DynamicArray():
    def __init__(self) -> None:
        self.n = 0
        self.capacity = 1
        self.A = self.make_array(self.capacity)

    def __len__(self):
        return self.n
    
    def __getitem__(self, k):
        if not 0 <= k < self.n:
            return IndexError
        return self.A[k]

    def getsize(self):
        return self.capacity

    def make_array(self, capacity):
        return (ctypes.py_object * capacity)()

    def append(self, item):
        self._checksize()
        self.A[self.n] = item
        self.n += 1
    
    def insertAt(self, item, index):
        if not 0 <= index < self.n:
            print("invalid index")
            return

        self._checksize()

        for i in range(self.n - 1, index - 1, -1):
            self.A[i + 1] = self.A[i]
        
        self.A[index] = item
        self.n += 1
    
    def removeAt(self, index):
        if self.n == 0:
            print("array is empty, deletion not possible")
            return
        if not 0 <= index < self.n:
            print("invalid index")
            return
        if index == self.n - 1:
            self.A[index] = 0
            n -= 1
            return

    def _checksize(self):
        if self.n == self.capacity:
            self._resize(2 * self.capacity)

    def _resize(self, new_cap):
        B = self.make_array(new_cap)
        for k in range(self.n):
            B[k] = self.A[k]
        self.A = B
        self.capacity = new_cap
    
    def print(self):
        for k in range(self.n):
            print(self.A[k], end=" ")

d = DynamicArray()
d.append(0)
d.append(1)
d.append(2)
d.append("hello")
print(d[0])
d.print()
print(len(d))
print(d.getsize())
d.append(3)
print(d.getsize())

d.insertAt("test", 0)
d.print()
