from heap_invert import Heap
from cancion import Cancion
import csv
import random
import time

def crear_lista():
    # Abrir el archivo y pasarlo a una lista propia
    with open("spotify_data.csv") as tsvF:
        lista_cancion = []
        for i in range(1159765):
            reader = csv.reader(tsvF)
            encabezado = next(reader)
            cancion = Cancion()
            if i > 0:
                cancion.set_autor(encabezado[1])
                cancion.set_nombre(encabezado[2])
                cancion.set_genero(encabezado[6])
                cancion.set_anio(encabezado[5])
                cancion.set_duration(encabezado[17])
            lista_cancion.append(cancion)
    return lista_cancion


if __name__ == "__main__":
    lista = crear_lista()
    tiempos = []
    for i in range(2, 7):
        tiempo = 0
        for _ in range(10):
            heap = Heap(10**i)
            heap.tamanio = 10**i
            heap.vector = [random.randint(0, 10000000) for _ in range(10**i)]

            ini = time.time()
            heap.monticulizar()
            heap.HeapSort()
            fin = time.time()
            t = fin - ini
            tiempo += t
        tiempo /= 10
        print(tiempo)
        tiempos.append(tiempo)

    print(tiempos)
