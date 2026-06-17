class Heap:
    def __init__(self):
        self.heap = []

    def __len__(self):
        return len(self.heap)

    def is_empty(self):
        return len(self.heap) == 0

    def parent(self, i):
        return (i - 1) // 2

    def left(self, i):
        return 2 * i + 1

    def right(self, i):
        return 2 * i + 2

    def peek(self):
        if self.is_empty():
            raise IndexError("Heap vazia")
        return self.heap[0]

    def __str__(self):
        return str(self.heap)