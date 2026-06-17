from max_heap import MaxHeap


def heap_sort(values):
    heap = MaxHeap()

    for value in values:
        heap.insert(value)

    result = []

    while not heap.is_empty():
        result.append(heap.extract_max())

    return result[::-1]