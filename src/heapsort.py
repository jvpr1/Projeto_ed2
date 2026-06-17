from max_heap import MaxHeap


def heap_sort(values): 
    heap = MaxHeap() # cria uma estrutura max heap , o maior sera raiz

    for value in values: # os elemento são inseridos
        heap.insert(value)

    result = [] # armazena

    while not heap.is_empty(): 
        result.append(heap.extract_max())

    return result[::-1]
