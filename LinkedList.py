class LL():

    def __init__(self) -> None:
        self.head = None

    class Node():
        def __init__(self, item) -> None:
            self.item = item
            self.next = None
        
        def __str__(self) -> str:
            return str(self.item)
    
    def addItem(self, item):
        n = self.head
        newNode = self.Node(item)
        if n == None:
            self.head = newNode
            return
        while n.next != None:
            n = n.next
        n.next = newNode

    def findItem(self, item):
        n = self.head
        if n.item == item:
            return n.item
        while n.next != None:
            n = n.next
            if n.item == item:
                return item
        print("item does not exist in LL")
        return
    
    def print(self):
        n = self.head
        if self.head == None:
            print("LL has no items")
            return
        print(n.item)
        while n.next != None:
            n = n.next
            print(n.item)

    def add_front(self, item):
        newNode = self.Node(item)
        newNode.next = self.head
        self.head = newNode
    
    def add_end(self, item):
        newNode = self.Node(item)
        if self.head is None:
            self.head = newNode
            return
        for current in self:
            pass
        current.next = newNode
    
    def remove_first(self):
        if self.head is None:
            print("LL has no items")
            return
        print(f"deleted first item: {self.head.item}")
        self.head = self.head.next
    
    def remove_last(self):
        if self.head is None:
            print("LL has no items")
            return
        if self.head.next is None:
            print(f"deleted last item: {self.head.item}")
            self.head = None
        for current in self:
            if current.next.next is None:
                prev = current
                break
        print(f"deleted last item: {prev.next.item}")
        prev.next = None

    
    def delete_node(self, item):
        if self.head is None:
            print("LL has no items")
            return
        if self.head.item == item:
            print(f"deleted: {self.head.item}")
            self.head = self.head.next
            return
        for current in self:
            prev = current
            if current.next is not None and current.next.item == item:
                print(f"deleted: {current.next.item}")
                prev.next = current.next.next
                return
        print(f"{item} does not exist in LL")

    def __repr__(self) -> str:
        n = self.head
        nodes = []
        while n is not None:
            nodes.append(str(n.item))
            n = n.next
        nodes.append("None")
        return " -> ".join(nodes)
    
    def __iter__(self):
        n = self.head
        while n is not None:
            yield n
            n = n.next

    # iterative method to reverse linked list
    def reverseIterative(self):
        prev = None
        current = self.head
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    # recursive method to reverse
    def reverseRecursive(self, head):
        if head is None or head.next is None:
            return head
        rest = self.reverseRecursive(head.next)
        head.next.next = head
        head.next = None
        return rest

    def _reverseUtil(self, curr, prev):
        if curr.next is None:
            self.head = curr
            curr.next = prev
            return
        next = curr.next
        curr.next = prev
        self._reverseUtil(next, curr)
    
    def _reverseUtil2(self, curr, prev):
        if curr.next is None:
            self.head = curr
            curr.next = prev
            return
        self._reverseUtil(curr.next, curr)
        next = curr.next
        curr.next = prev

    def reverseUtil2(self):
        if self.head is None:
            return
        self._reverseUtil2(self.head, None)

    def reverseUtil(self):
        if self.head is None:
            return
        self._reverseUtil(self.head, None)
x = LL()
x.addItem(1)
x.addItem(2)
x.addItem(3)
x.add_front(0)
x.add_end(4)
x.print()
print(x.findItem(0))


# reversing
print("-- Reversing section --")
print(repr(x))
x.reverseIterative()
print(repr(x))
x.head = x.reverseRecursive(x.head)
print(repr(x))
x.reverseUtil2()
print(repr(x))
x.reverseUtil()
print(repr(x))

#deleting
print("-- Deleting section --")
x.delete_node(0)
print(repr(x))
y = LL()
y.delete_node(0)
print(repr(x))
x.remove_first()
print(repr(x))
x.remove_last()
print(repr(x))