from src.min_heap import MinHeap
from src.heapsort import heap_sort
from src.max_heap import MaxHeap
from src.heapsort import heap_sort
from src.min_heap import MinHeap
from src.max_heap import MaxHeap

heap = MinHeap()

for valor in [20, 10, 30, 5, 15]:
    heap.insert(valor)

print(heap)

while not heap.is_empty():
    print(heap.extract_min())


heap = MaxHeap()

for valor in [20, 10, 30, 5, 15]:
    heap.insert(valor)

print(heap)

while not heap.is_empty():
    print(heap.extract_max())


numeros = [8, 4, 15, 1, 10, 7]

print(heap_sort(numeros))


def test_min_heap():
    heap = MinHeap()

    heap.insert(10)
    heap.insert(5)
    heap.insert(20)

    assert heap.extract_min() == 5
    assert heap.extract_min() == 10
    assert heap.extract_min() == 20


def test_max_heap():
    heap = MaxHeap()

    heap.insert(10)
    heap.insert(5)
    heap.insert(20)

    assert heap.extract_max() == 20
    assert heap.extract_max() == 10
    assert heap.extract_max() == 5


def test_heapsort():
    valores = [9, 4, 7, 1, 3]

    assert heap_sort(valores) == [1, 3, 4, 7, 9]