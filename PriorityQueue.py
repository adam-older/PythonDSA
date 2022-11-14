from decimal import InvalidOperation
from typing import Generic, List, TypeVar

T = TypeVar('T')

class PriorityQueue(Generic[T]):
    # def __init__(self, elems: List[T] = []) -> None:
    #     self._heap = elems

    # @classmethod
    # def heapify(cls, elems: List[T]):
    #     heapSize = len(elems)
    #     heap = []
    #     heap.extend(elems)
    #     for i in range(max(0, (heapSize / 2) -1), 0, -1):
    #         print(i)
    #         self._sink(i)

    #     return cls()

    def __init__(self, elems: List[T] = None) -> None:
        self._heap = []
        if elems is not None:
            self._heapify(elems)
    
    def _heapify(self, elems: List[T]) -> List[T]:
        heapSize = len(elems)
        self._heap.extend(elems)
        for i in range(max(0, (heapSize // 2) -1), -1, -1):
            print(i)
            self._sink(i)

    def add(self, elem: T) -> None:
        if elem is None: raise InvalidOperation('Elem cannot be None')

        self._heap.append(elem)

        lastIndex = self._size() - 1
        self._swim(lastIndex)
    
    def peek(self) -> T:
        if (self.isEmpty()): return None
        return self._heap[0]

    def poll(self) -> T:
        return self.removeAt(0)

    def removeAt(self, k: int) -> T:
        if (self.isEmpty()): return None

        index_last_elem = self._size() - 1
        removed_item = self._heap[k]
        self._swap(k, index_last_elem)

        # remove last elem
        self._heap.pop(index_last_elem)

        # return deleted elem if k = last index
        if k == index_last_elem: return removed_item

        # get replaced elem at k
        elem = self._heap[k]

        # try sinking
        self._sink(k)

        # if sink doesnt work, swim instead
        if self._heap[k] == elem: self._swim(k)
        return removed_item

    # Perform a top down node sink, O(log(n))
    def _sink(self, k: int) -> None:
        heapSize = self._size()
        while True:
            left = 2 * k + 1 # left child node
            right = 2 * k + 2 # right child node
            smallest = left # default smallest as left

            # find smaller child node
            # if right is smaller, set smallest = right
            if right < heapSize and self._less(right, left): 
                smallest = right
            
            # stop if outside bounds of tree,
            # stop if k is in the right place (cannot sink anymore)
            if left >= heapSize or self._less(k, smallest):
                break

            self._swap(smallest, k)
            k = smallest

    def _swim(self, k:int) -> None:
        parent = (k - 1) // 2

        while k > 0 and self._less(k, parent):
            self._swap(parent, k)
            k = parent

            parent = (k - 1) // 2

    # compare data items at indicies i and j
    # return true if heap[i] less than heap[j]
    def _less(self, i: int, j: int) -> bool:
        data1 = self._heap[i]
        data2 = self._heap[j]
        return data1 < data2

    # swap elements at indicies i and j
    def _swap(self, i: int, j:int) -> None:
        self._heap[i], self._heap[j] = self._heap[j], self._heap[i]

    def clear(self) -> None:
        self._heap.clear()

    def isEmpty(self) -> bool:
        return self._size() == 0

    def _size(self) -> int:
        return len(self._heap)

    def __len__(self) -> int:
        return len(self._heap)

    def __str__(self) -> str:
        return str(self._heap)


elems = [4, 3, 1, 7, 5]

pq = PriorityQueue(elems=elems)
print(pq)
print(pq.peek())


while not pq.isEmpty():
    print(pq.poll())

print(pq)
