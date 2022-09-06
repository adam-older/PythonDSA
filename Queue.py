from collections import deque

class Queue:
    def __init__(self) -> None:
        self._data = deque()

    def enqueue(self, val):
        self._data.append(val)

    def dequeue(self):
        return self._data.popleft()

    def __repr__(self) -> str:
        return str(self._data)

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
print(f"Dequeued: {q.dequeue()}")
print(repr(q))