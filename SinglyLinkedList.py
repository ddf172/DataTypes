class Node:
    def __init__(self, value=0, next_node=None):
        self.value = value
        self.next = next_node


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def get_to_node_at(self, position):
        if self.head is None:
            raise IndexError("List is empty")
        if position < 0 or position > self.size:
            raise IndexError("Index out of range, list size: {}, position to get: {}".format(self.size, position))
        curr_node = self.head
        curr_position = 0
        while curr_position != position:
            curr_position += 1
            curr_node = curr_node.next
        return curr_node

    def insert_back(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
        else:
            self.tail.next = node
        self.tail = node
        self.size += 1

    def insert_front(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node
        if self.tail is None:
            self.tail = self.head
        self.size += 1

    def insert_at(self, value, position=0):
        node = Node(value)
        if position == 0:
            self.insert_front(node)
            return
        if position == self.size:
            self.insert_back(node)
            return
        curr_node = self.get_to_node_at(position-1)
        if curr_node is None:
            raise IndexError("Index out of range, list size: {}, position to insert: {}".format(self.size, position))
        node.next = curr_node.next
        curr_node.next = node
        self.size += 1

    def pop_check(self):
        if self.size < 1:
            raise IndexError("Can not delete from empty list")
        if self.size == 1:
            self.head = None
            self.tail = None
            self.size -= 1
            return True

    def pop_back(self):
        if self.pop_check():
            return
        curr_node = self.head
        while curr_node.next is not self.tail:
            curr_node = curr_node.next
        curr_node.next = None
        self.tail = curr_node
        self.size -= 1

    def pop_front(self):
        if self.pop_check():
            return
        temp_node = self.head
        self.head = self.head.next
        temp_node.next = None
        del temp_node
        self.size -= 1

    def pop_at(self, position=0):
        if position == 0:
            self.pop_front()
            return
        if position == self.size-1:
            self.pop_back()
            return
        prev_node = self.get_to_node_at(position-1)
        del_node = prev_node.next
        if del_node is None:
            raise IndexError("Index out of range, list size: {}, position to remove: {}".format(self.size, position))
        prev_node.next = del_node.next
        del_node.next = None
        del del_node
        self.size -= 1

    def value_at(self, position=0):
        curr_node = self.get_to_node_at(position)
        return curr_node.value

    def change_value_at(self, value, position=0):
        curr_node = self.get_to_node_at(position)
        curr_node.value = value

    def extend(self, value_list):
        if type(value_list) is not list:
            raise TypeError("Argument have to be a list of Nodes")
        for value in value_list:
            if type(value) is Node:
                raise TypeError("Every item has to be primary type(int,str,chr...)")
            self.insert_back(value)

    def move_node(self, start_position, destination):
        pass

    def reverse_list(self):
        if self.head is None or self.head.next is None: return self.head
        prev_node = self.head
        node = self.head.next
        prev_node.next = None
        while node is not None:
            temp = node.next
            node.next = prev_node
            prev_node = node
            node = temp

    def find(self, value):
        curr_node = self.head
        position = 0
        while curr_node.value != value:
            if curr_node is None:
                return -1
            position += 1
            curr_node = curr_node.next
        return position

    def to_list(self):
        result = []
        curr_node = self.head
        while curr_node is not None:
            result.append(curr_node.value)
            curr_node = curr_node.next
        return result

    def clear(self):
        if self.head is None:
            return
        prev_node = self.head
        curr_node = self.head.next
        while curr_node is not None:
            prev_node.next = None
            prev_node = curr_node
            curr_node = curr_node.next
        self.head = None
        self.tail = None

    def print_list(self):
        if self.head is None:
            print("List is empty")
            return
        tracker = self.head
        while tracker is not None:
            print(tracker.value)
            tracker = tracker.next

    def check_size(self):
        counter = 0
        curr_node = self.head
        while curr_node is not None:
            counter += 1
            curr_node = curr_node.next
        if self.size != counter:
            self.size = counter

    def is_empty(self):
        if self.size:
            return False
        return True

    def __del__(self):
        self.clear()

    def __len__(self):
        self.check_size()
        return self.size
