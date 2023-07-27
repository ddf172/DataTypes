class ListMinHeap:
    def __init__(self):
        self.__heap = []

    def peek(self):
        if not self.is_empty():
            return self.__heap[0]

    def insert(self, value):
        self.__heap.append(value)
        self.__heapify_up(len(self.__heap)-1)

    def pop(self):
        if not self.__heap:
            return None
        self.__heap[0], self.__heap[-1] = self.__heap[-1], self.__heap[0]
        value = self.__heap.pop()
        self.__heapify_down(0)
        return value

    def heapify_down(self, index):
        left = 2 * index + 1
        right = 2 * index + 2
        minimum = index
        if left < len(self.__heap) and self.__heap[left] < self.__heap[minimum]:
            minimum = left
        if right < len(self.__heap) and self.__heap[right] < self.__heap[minimum]:
            minimum = right
        if minimum != index:
            self.__heap[minimum], self.__heap[index] = self.__heap[index], self.__heap[minimum]
            self.__heapify_down(minimum)

    def heapify_up(self, index):
        parent = (index - 1) // 2
        while index > 0 and self.__heap[index] < self.__heap[parent]:
            self.__heap[index], self.__heap[parent] = self.__heap[parent], self.__heap[index]
            index = parent
            parent = (index - 1) // 2

    def is_empty(self):
        return not self.__heap

    def size(self):
        return len(self.__heap)

    def __len__(self):
        return self.size()

    def show(self):
        print(self.__heap)
