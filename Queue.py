from SinglyLinkedList import Node


class LinkedQueue:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def enqueue(self, value):
        node = Node(value)
        if self.is_empty():
            self.head = node
        else:
            self.tail.next = node
        self.tail = node

    def dequeue(self):
        if self.is_empty():
            return None

        value = self.head.value
        self.head.next, self.head = None, self.head.next
        if self.is_empty():
            self.tail = None

        return value

    def peek(self):
        if self.is_empty():
            return None
        return self.head.value

    def peek_at(self, index):
        curr = self.head
        while index > 0:
            if not curr:
                return -1
            curr = curr.next
            index -= 1
        return curr.value

    def size(self):
        curr = self.head
        size = 0
        while curr:
            size += 1
            curr = curr.next
        return curr

    def display(self):
        curr = self.head
        while curr:
            print(curr.value, end="->")
            curr = curr.next
        print("None")

    def to_list(self):
        if self.is_empty():
            return []
        curr = self.head
        arr = []
        while curr:
            arr.append(curr.value)
            curr = curr.next
        return arr

    def find(self, value):
        curr = self.head
        index = 0
        while curr:
            if curr.value == value:
                return index
            curr = curr.next
            index += 1
        return -1

    def remove_value(self, value):
        prev = None
        curr = self.head
        while curr:
            if curr.value == value:
                if curr == self.head:
                    self.dequeue()
                elif curr == self.tail:
                    prev.next = None
                    self.tail = prev
                else:
                    temp = curr.next
                    curr.next = None
                    prev.next = temp
                break
            prev = curr
            curr = curr.next

    def remove_at(self, index):
        prev = None
        curr = self.head
        if index == 0:
            return self.dequeue()
        while curr:
            if index == 0:
                value = curr.value
                temp = curr.next
                curr.next = None
                prev.next = temp
                return value
            index -= 1
            prev = curr
            curr = curr.next


class CircularQueue(LinkedQueue):
    def __init__(self):
        LinkedQueue.__init__(self)

    def enqueue(self, value):
        LinkedQueue.enqueue(self, value)
        self.tail.next = self.head

    def dequeue(self):
        if self.is_empty():
            return None

        value = self.head.value
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            temp = self.head
            self.head = self.head.next
            self.tail.next = self.head
            temp.next = None
        return value

    def scroll(self):
        if self.is_empty() or self.head == self.tail:
            return
        self.head = self.head.next
        self.tail = self.head

    def display(self):
        if self.is_empty():
            print("None")
            return

        curr = self.head
        while True:
            print(curr.value, end="->")
            curr = curr.next
            if curr == self.head:
                break
        print("head")

    def to_list(self):
        if self.is_empty():
            return []
        curr = self.head
        arr = []
        while True:
            arr.append(curr.value)
            curr = curr.next
            if curr == self.head:
                break
        return arr

    def size(self):
        if self.is_empty():
            return 0
        size = 0
        curr = self.head
        while True:
            size += 1
            curr = curr.next
            if curr == self.head:
                break
        return size

    def find(self, value):
        if self.is_empty():
            return -1
        curr = self.head
        index = 0
        while True:
            if curr.value == value:
                return index
            curr = curr.next
            if curr == self.head:
                return -1

    def peek_at(self, index):
        if self.is_empty():
            return -1
        curr = self.head
        while index > 0:
            curr = curr.next
            if curr == self.head:
                return -1
            index -= 1
        return curr.value

    def remove_value(self, value):
        if self.is_empty():
            return
        prev = None
        curr = self.head
        while True:
            if curr.value == value:
                if curr == self.head:
                    self.dequeue()
                elif curr == self.tail:
                    prev.next = self.head
                    self.tail.next = None
                    self.tail = prev
                else:
                    temp = curr.next
                    curr.next = None
                    prev.next = temp
                break

            prev = curr
            curr = curr.next
            if curr == self.head:
                break

    def remove_at(self, index):
        if self.is_empty() or index < 0:
            return None
        if index == 0:
            return self.dequeue()

        prev = None
        curr = self.head
        while index > 0:
            prev = curr
            curr = curr.next
            index -= 1
            if curr == self.head:
                return None

        value = curr.value
        if curr == self.tail:
            prev.next = self.head
            self.tail.next = None
            self.tail = prev
        else:
            temp = curr.next
            curr.next = None
            prev.next = temp
        return value
