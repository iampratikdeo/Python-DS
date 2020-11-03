class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class doubly_linked_list:
    def __init__(self):
        self.head = None

    def push(self, data):
        NewNode = Node(data)
        NewNode.next = self.head
        if self.head is not None:
            self.head.prev = NewNode
        self.head = NewNode

    def insert(self, previous, data):
        if previous is None:
            return
        NewNode = Node(data)
        NewNode.next = previous.next
        previous.next = NewNode
        NewNode.prev = previous
        if NewNode.next is not None:
            NewNode.next.prev = NewNode

    def listprint(self, node):
        while node is not None:
            print(node.data)
            last = node
            node = node.next

    def append(self, data):
        NewNode = Node(data)
        NewNode.next = None
        if self.head is None:
            NewNode.prev = None
            self.head = NewNode
            return
        last = self.head
        while last.next is not None:
            last = last.next
        last.next = NewNode
        NewNode.prev = last
        return


dllist = doubly_linked_list()
dllist.push(12)
dllist.append(9)
dllist.push(8)
dllist.push(62)
dllist.append(45)
dllist.listprint(dllist.head)
