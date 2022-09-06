class Stack:
    def __init__(self):
        self._data = []
    
    def push(self, val):
        self._data.append(val)
    
    def pop(self):
        return self._data.pop()

    def peek(self):
        return self._data[len(self._data) - 1]

    def __repr__(self) -> str:
        return str(self._data)

s = Stack()
s.push(1)
s.push(2)
s.push(3)
print(repr(s))
print(f"Popped: {s.pop()}")
print(repr(s))
