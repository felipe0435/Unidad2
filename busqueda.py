from heap_invert import Heap
import random
import time

tiempos_secu = []
tiempos_iter = []
tiempos_rec = []
vector = random.sample(range(1000,10000000000000),1000000)
heap = Heap(1000000)
heap.vector = vector
heap.monticulizar()
heap.HeapSort()

for i in range(3):
    tiempo_secu = 0
    tiempo_iter = 0
    tiempo_rec = 0
    for _ in range(10):
        elem = heap.vector[(i * (heap.tamanio - 1)) // 2]

        ini_secu = time.time()
        heap.busqueda_secu(elem)
        fin_secu = time.time()
        t_secu = fin_secu - ini_secu
        tiempo_secu += t_secu

        ini_iter = time.time()
        heap.busqueda_bin_iter(elem)
        fin_iter = time.time()
        t_iter = fin_iter - ini_iter
        tiempo_iter += t_iter

        ini_rec = time.time()
        heap.busqueda_bin_rec(elem, 0, heap.tamanio)
        fin_rec = time.time()
        t_rec = fin_rec - ini_rec
        tiempo_rec += t_rec

    print("secu:", tiempo_secu / 10, "iter:", tiempo_iter / 10, "rec:", tiempo_rec / 10)
    tiempos_secu.append(tiempo_secu / 10)
    tiempos_iter.append(tiempo_iter / 10)
    tiempos_rec.append(tiempo_rec / 10)

print("Búsqueda secuencial:", tiempos_secu, "\nBúsqueda binaria iterativa:", tiempos_iter, "\nBúsqueda binaria recursiva:", tiempos_rec)