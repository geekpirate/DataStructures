class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def getAll(self):
        out = []
        root = self.head
        while root:
            # print(root.val)
            out.append(root.val)
            root = root.next
        return out

    def push(self, val: int):
        curr = Node(val)

        if self.head is None:
            self.head = curr
        else:
            ptr = self.head
            while ptr.next is not None:
                ptr = ptr.next
            ptr.next = curr

        self.size += 1

    def addAtIndex(self, val: int, index: int):
        if self.size-1 < index:
            raise Exception("List index overflow. Please enter index value < ")
        curr = Node(val)
        ptr = self.head
        while index > 1:
            index -= 1
            ptr = ptr.next
        temp = ptr.next
        ptr.next = curr
        curr.next = temp
        self.size += 1

    def deleteAtIndex(self, index: int):
        # print(self.size)
        if self.size-1 < index:
            raise Exception("List index overflow. Please enter index value < ")
        ptr = self.head
        while index > 1:
            index -= 1
            ptr = ptr.next

        ptr.next = ptr.next.next
        self.size -= 1



ll = LinkedList()
ll.push(3)
ll.push(4)
ll.push(1)
ll.push(0)
print(ll.getAll())
ll.addAtIndex(7, 2)
print(ll.getAll())
ll.deleteAtIndex(2)
print(ll.getAll())

ll.deleteAtIndex(4)
print(ll.getAll())

