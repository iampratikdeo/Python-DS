class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def listprint(self):
        printval = self.head
        while printval is not None:
            print(printval.data)
            printval = printval.next

    def insertAtStart(self, newdata):
        NewNode = Node(newdata)
        # updating pointer
        NewNode.next = self.head
        self.head = NewNode

    def insertAtEnd(self, newdata):
        NewNode = Node(newdata)
        if self.head is None:
            self.head = NewNode
            return
        lastNode = self.head
        while lastNode.next:
            lastNode = lastNode.next
        lastNode.next = NewNode

    def inBetween(self, middleNode, newdata):
        if middleNode is None:
            print("Please provide middle Node")
            return
        NewNode = Node(newdata)
        NewNode.next = middleNode.next
        middleNode.next = NewNode

    def remove(self, data):
        head = self.head

        if(head is not None):
            if head.data == data:
                self.head = head.next
                head = None
                return

        while head is not None:
            if head.data == data:
                break

            prev = head
            head = head.next
        if head == None:
            return
        prev.next = head.next
        head = None


l = LinkedList()

l.head = Node("Mon")
e2 = Node("Tues")
e3 = Node("Wed")

l.head.next = e2

e2.next = e3
l.insertAtStart("Sun")
l.insertAtEnd("Thur")
l.inBetween(e2, "Fri")
l.remove("Tues")
l.listprint()

# inserting at the start
