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
grafo.insertarArista(2.0, grafo.buscarVertice("Chile"), "Argenina")
grafo.insertarArista(3.7, grafo.buscarVertice("Chile"), "Peru")
grafo.insertarArista(4.4, grafo.buscarVertice("Chile"), "Brazil")
grafo.insertarArista(2.5, grafo.buscarVertice("Chile"), "Uruguay")
grafo.insertarArista(2.4, grafo.buscarVertice("Chile"), "Paraguay")
grafo.insertarArista(5.1, grafo.buscarVertice("Chile"), "Ecuador")
grafo.insertarArista(3.2, grafo.buscarVertice("Chile"), "Bolivia")
grafo.insertarArista(6.0, grafo.buscarVertice("Chile"), "Colombia")
grafo.insertarArista(9.5, grafo.buscarVertice("Chile"), "Venezuela")
grafo.insertarArista(12.5, grafo.buscarVertice("Chile"), "Espania")
grafo.insertarArista(8.3, grafo.buscarVertice("Chile"), "Mexico")
grafo.insertarArista(4.5, "Argentina", "Peru")
grafo.insertarArista(2.8, "Argentina", "Brazil")
grafo.insertarArista(1.0, "Argentina", "Uruguay")
grafo.insertarArista(6.1, "Argentina", "Ecuador")
grafo.insertarArista(3.0, "Argentina", "Bolivia")
grafo.insertarArista(4.8, "Peru", "Brazil")
grafo.insertarArista(4.7, "Peru", "Uruguay")
grafo.insertarArista(3.8, "Peru", "Paraguay")
grafo.insertarArista(2.3, "Peru", "Ecuador")
grafo.insertarArista(1.8, "Peru", "Bolivia")
grafo.insertarArista(3.2, "Peru", "Colombia")
grafo.insertarArista(4.0, "Peru", "Venezuela")
grafo.insertarArista(11.8, "Peru", "Espania")
grafo.insertarArista(6.1, "Peru", "Mexico")
grafo.insertarArista(2.9, "Brazil", "Uruguay")
grafo.insertarArista(2.7, "Brazil", "Paraguay")
grafo.insertarArista(6.3, "Brazil", "Colombia")
grafo.insertarArista(10.1, "Brazil", "Espania")
grafo.insertarArista(1.8, "Uruguay", "Paraguay")
grafo.insertarArista(6.6, "Uruguay", "Colombia")
grafo.insertarArista(12.5, "Uruguay", "Espania")
grafo.insertarArista(1.8, "Paraguay", "Bolivia")
grafo.insertarArista(5.3, "Paraguay", "Colombia")
grafo.insertarArista(11.3, "Paraguay", "Espania")
grafo.insertarArista(1.6, "Ecuador", "Colombia")
grafo.insertarArista(10.7, "Ecuador", "Espania")
grafo.insertarArista(4.8, "Ecuador", "Mexico")
grafo.insertarArista(4.0, "Bolivia", "Colombia")
grafo.insertarArista(4.4, "Bolivia", "Venezuela")
grafo.insertarArista(11.1 , "Bolivia", "Espania")
grafo.insertarArista(2.0, "Colombia", "Venezuela")
grafo.insertarArista(10.0, "Colombia", "Espania")
grafo.insertarArista(4.7, "Colombia", "Mexico")
grafo.insertarArista(9.0, "Venezuela", "Espania")
grafo.insertarArista(5.0, "Venezuela", "Mexico")
grafo.insertarArista(11.4, "Espania", "Mexico")


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

