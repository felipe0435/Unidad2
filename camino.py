from grafo import Grafo
import time
import random

grafo = Grafo()

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


#grafo.insertarAristas("Hora, pais salida, Pais de arribo")
grafo.insertarArista(2.0, grafo.buscarVertice("Chile"), grafo.buscarVertice("Argentina"))
grafo.insertarArista(3.7, grafo.buscarVertice("Chile"), grafo.buscarVertice("Peru"))
grafo.insertarArista(4.4, grafo.buscarVertice("Chile"), grafo.buscarVertice("Brazil"))
grafo.insertarArista(2.5, grafo.buscarVertice("Chile"), grafo.buscarVertice("Uruguay"))
grafo.insertarArista(2.4, grafo.buscarVertice("Chile"), grafo.buscarVertice("Paraguay"))
grafo.insertarArista(5.1, grafo.buscarVertice("Chile"), grafo.buscarVertice("Ecuador"))
grafo.insertarArista(3.2, grafo.buscarVertice("Chile"), grafo.buscarVertice("Bolivia"))
grafo.insertarArista(6.0, grafo.buscarVertice("Chile"), grafo.buscarVertice("Colombia"))
grafo.insertarArista(9.5, grafo.buscarVertice("Chile"), grafo.buscarVertice("Venezuela"))
grafo.insertarArista(12.5, grafo.buscarVertice("Chile"), grafo.buscarVertice("Espania"))
grafo.insertarArista(8.3, grafo.buscarVertice("Chile"), grafo.buscarVertice("Mexico"))
grafo.insertarArista(4.5, grafo.buscarVertice("Argentina"), grafo.buscarVertice("Peru"))
grafo.insertarArista(2.8, grafo.buscarVertice("Argentina"), grafo.buscarVertice("Brazil"))
grafo.insertarArista(1.0, grafo.buscarVertice("Argentina"), grafo.buscarVertice("Uruguay"))
grafo.insertarArista(6.1, grafo.buscarVertice("Argentina"), grafo.buscarVertice("Ecuador"))
grafo.insertarArista(3.0, grafo.buscarVertice("Argentina"), grafo.buscarVertice("Bolivia"))
grafo.insertarArista(4.8, grafo.buscarVertice("Peru"), grafo.buscarVertice("Brazil"))
grafo.insertarArista(4.7, grafo.buscarVertice("Peru"), grafo.buscarVertice("Uruguay"))
grafo.insertarArista(3.8, grafo.buscarVertice("Peru"), grafo.buscarVertice("Paraguay"))
grafo.insertarArista(2.3, grafo.buscarVertice("Peru"), grafo.buscarVertice("Ecuador"))
grafo.insertarArista(1.8, grafo.buscarVertice("Peru"), grafo.buscarVertice("Bolivia"))
grafo.insertarArista(3.2, grafo.buscarVertice("Peru"), grafo.buscarVertice("Colombia"))
grafo.insertarArista(4.0, grafo.buscarVertice("Peru"), grafo.buscarVertice("Venezuela"))
grafo.insertarArista(11.8, grafo.buscarVertice("Peru"), grafo.buscarVertice("Espania"))
grafo.insertarArista(6.1, grafo.buscarVertice("Peru"), grafo.buscarVertice("Mexico"))
grafo.insertarArista(2.9, grafo.buscarVertice("Brazil"), grafo.buscarVertice("Uruguay"))
grafo.insertarArista(2.7, grafo.buscarVertice("Brazil"), grafo.buscarVertice("Paraguay"))
grafo.insertarArista(6.3, grafo.buscarVertice("Brazil"), grafo.buscarVertice("Colombia"))
grafo.insertarArista(10.1, grafo.buscarVertice("Brazil"), grafo.buscarVertice("Espania"))
grafo.insertarArista(1.8, grafo.buscarVertice("Uruguay"), grafo.buscarVertice("Paraguay"))
grafo.insertarArista(6.6, grafo.buscarVertice("Uruguay"), grafo.buscarVertice("Colombia"))
grafo.insertarArista(12.5, grafo.buscarVertice("Uruguay"), grafo.buscarVertice("Espania"))
grafo.insertarArista(1.8, grafo.buscarVertice("Paraguay"), grafo.buscarVertice("Bolivia"))
grafo.insertarArista(5.3, grafo.buscarVertice("Paraguay"), grafo.buscarVertice("Colombia"))
grafo.insertarArista(11.3, grafo.buscarVertice("Paraguay"), grafo.buscarVertice("Espania"))
grafo.insertarArista(1.6, grafo.buscarVertice("Ecuador"), grafo.buscarVertice("Colombia"))
grafo.insertarArista(10.7, grafo.buscarVertice("Ecuador"), grafo.buscarVertice("Espania"))
grafo.insertarArista(4.8, grafo.buscarVertice("Ecuador"), grafo.buscarVertice("Mexico"))
grafo.insertarArista(4.0, grafo.buscarVertice("Bolivia"), grafo.buscarVertice("Colombia"))
grafo.insertarArista(4.4, grafo.buscarVertice("Bolivia"), grafo.buscarVertice("Venezuela"))
grafo.insertarArista(11.1 , grafo.buscarVertice("Bolivia"), grafo.buscarVertice("Espania"))
grafo.insertarArista(2.0, grafo.buscarVertice("Colombia"), grafo.buscarVertice("Venezuela"))
grafo.insertarArista(10.0, grafo.buscarVertice("Colombia"), grafo.buscarVertice("Espania"))
grafo.insertarArista(4.7, grafo.buscarVertice("Colombia"), grafo.buscarVertice("Mexico"))
grafo.insertarArista(9.0, grafo.buscarVertice("Venezuela"), grafo.buscarVertice("Espania"))
grafo.insertarArista(5.0, grafo.buscarVertice("Venezuela"), grafo.buscarVertice("Mexico"))
grafo.insertarArista(11.4, grafo.buscarVertice("Espania"), grafo.buscarVertice("Mexico"))


grafo.adyacentes(grafo.buscarVertice("Chile"))

"""
10 = 0.1
15 = 0.2
20 = 0.3
25 = 0.4
30 = 0.5
35 = 0.6
40 = 0.7
45 = 0.8
50 = 0.8
55 = 0.9
"""

