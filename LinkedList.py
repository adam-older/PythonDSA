class LL():

    def __init__(self, item) -> None:
        self.head = self.Node(item, None)

    class Node():
        def __init__(self, item, next) -> None:
            self.item = item
            self.next = next
    
    def addItem(self, item):
        n = self.head
        while (n.next
        self.head.next = 