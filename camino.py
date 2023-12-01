from grafo import Grafo
import time
import random


def crear_grafo(grafo):
    # Vertices del grafo
    grafo.insertarVertice("Chile")
    grafo.insertarVertice("Argentina")
    grafo.insertarVertice("Peru")
    grafo.insertarVertice("Brazil")
    grafo.insertarVertice("Uruguay")
    grafo.insertarVertice("Paraguay")
    grafo.insertarVertice("Ecuador")
    grafo.insertarVertice("Bolivia")
    grafo.insertarVertice("Colombia")
    grafo.insertarVertice("Venezuela")
    grafo.insertarVertice("Espania")
    grafo.insertarVertice("Mexico")
    # Aristas entre vertices
    grafo.insertarArista(2.0, grafo.buscarVertice("Chile"), grafo.buscarVertice("Argentina"))
    grafo.insertarArista(3.7, grafo.buscarVertice("Chile"), grafo.buscarVertice("Peru"))
    grafo.insertarArista(2.4, grafo.buscarVertice("Argentina"), grafo.buscarVertice("Paraguay"))
    grafo.insertarArista(3.2, grafo.buscarVertice("Chile"), grafo.buscarVertice("Bolivia"))
    grafo.insertarArista(2.8, grafo.buscarVertice("Argentina"), grafo.buscarVertice("Brazil"))
    grafo.insertarArista(1.0, grafo.buscarVertice("Argentina"), grafo.buscarVertice("Uruguay"))
    grafo.insertarArista(3.0, grafo.buscarVertice("Argentina"), grafo.buscarVertice("Bolivia"))
    grafo.insertarArista(2.9, grafo.buscarVertice("Brazil"), grafo.buscarVertice("Venezuela"))
    grafo.insertarArista(2.7, grafo.buscarVertice("Brazil"), grafo.buscarVertice("Paraguay"))
    grafo.insertarArista(6.3, grafo.buscarVertice("Brazil"), grafo.buscarVertice("Colombia"))
    grafo.insertarArista(10.1, grafo.buscarVertice("Brazil"), grafo.buscarVertice("Espania"))
    grafo.insertarArista(1.8, grafo.buscarVertice("Uruguay"), grafo.buscarVertice("Paraguay"))
    grafo.insertarArista(1.8, grafo.buscarVertice("Paraguay"), grafo.buscarVertice("Bolivia"))
    grafo.insertarArista(1.6, grafo.buscarVertice("Ecuador"), grafo.buscarVertice("Colombia"))
    grafo.insertarArista(2.0, grafo.buscarVertice("Colombia"), grafo.buscarVertice("Venezuela"))
    grafo.insertarArista(4.7, grafo.buscarVertice("Colombia"), grafo.buscarVertice("Mexico"))
    grafo.insertarArista(11.4, grafo.buscarVertice("Espania"), grafo.buscarVertice("Mexico"))


if __name__ == "__main__":
    grafo = Grafo()
    crear_grafo(grafo)
    grafo.dijkstra(grafo.buscarVertice("Venezuela"), grafo.buscarVertice("Argentina"))