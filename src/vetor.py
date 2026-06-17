
def pai(i):
    return (i - 1) // 2

def filho_esquerdo(i):
    return 2 * i + 1

def filho_direito(i):
    return 2 * i + 2


heap = [50, 30, 40, 10, 20, 35]

indice = 4

print("Elemento:", heap[indice])
print("Pai:", heap[pai(indice)])
print("Índice do pai:", pai(indice))
