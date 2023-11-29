from heap_invert import Heap
import random
import time


if __name__ == "__main__":
    tiempos = []
    for i in range(2, 7):
        tiempo = 0
        for _ in range(10):
            # Se genera el monticulo
            heap = Heap(10**i)
            heap.tamanio = 10**i
            heap.vector = [random.randint(0, 10000000) for _ in range(10**i)]
            # Se ordena el heap
            inicio = time.time()
            heap.monticulizar()
            heap.HeapSort()
            fin = time.time()
            # Calculo de tiempo
            tiempo += fin - inicio
        tiempo /= 10
        print(tiempo)
        tiempos.append(tiempo)
    print(tiempos)
