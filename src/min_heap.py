from heap import Heap


class MinHeap(Heap):

    def insert(self, value):
        self.heap.append(value)
        self._up_heapify(len(self.heap) - 1)

    def extract_min(self):
        if self.is_empty():
            raise IndexError("Heap vazia")

        minimum = self.heap[0]

        last = self.heap.pop()

        if self.heap:
            self.heap[0] = last
            self._down_heapify(0)

        return minimum

    def _up_heapify(self, index):
        while index > 0:
            parent = self.parent(index)

            if self.heap[index] < self.heap[parent]:
                self.heap[index], self.heap[parent] = (
                    self.heap[parent],
                    self.heap[index]
                )
                index = parent
            else:
                break

    def _down_heapify(self, index):
        size = len(self.heap)

        while True:
            smallest = index

            left = self.left(index)
            right = self.right(index)

            if left < size and self.heap[left] < self.heap[smallest]:
                smallest = left

            if right < size and self.heap[right] < self.heap[smallest]:
                smallest = right

            if smallest != index:
                self.heap[index], self.heap[smallest] = (
                    self.heap[smallest],
                    self.heap[index]
                )
                index = smallest
            else:
                break