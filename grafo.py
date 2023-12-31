from math import inf
from cola import Cola
from heap_invert import Heap
from pila import Pila


class nodoArista(object):
    def __init__(self, info, destino):
        self.info = info
        self.destino = destino
        self.siguiente = None


class nodoVertice(object):
    def __init__(self, info):
        self.info = info
        self.siguiente = None
        self.visitado = False
        self.adyacentes = Arista()


class Arista(object):
    def __init__(self):
        self.inicio = None
        self.tamanio = 0


class Grafo(object):
    def __init__(self, dirigido=False):
        self.inicio = None
        self.dirigido = dirigido
        self.tamanio = 0


    def insertarVertice(self, info):
        nodo = nodoVertice(info)
        if self.inicio is None or self.inicio.info > info:
            nodo.siguiente = self.inicio
            self.inicio = nodo
        else:
            ant = self.inicio
            act = self.inicio.siguiente
            while act is not None and act.info < nodo.info:
                ant = act
                act = act.siguiente
            nodo.siguiente = act
            ant.siguiente = nodo
        self.tamanio += 1


    def agregarArista(self, origen, info, destino):
        nodo = nodoArista(info, destino)
        if origen.inicio is None or origen.inicio.destino > destino:
            nodo.siguiente = origen.inicio
            origen.inicio = nodo
        else:
            ant = origen.inicio
            act = origen.inicio.siguiente
            while act is not None and act.destino < nodo.destino:
                ant = act
                act = act.siguiente
            nodo.siguiente = act
            ant.siguiente = nodo
        origen.tamanio += 1


    def insertarArista(self, info, origen, destino):
        self.agregarArista(origen.adyacentes, info, destino.info)
        if not self.dirigido:
            self.agregarArista(destino.adyacentes, info, origen.info)


    def eliminarArista(self, vertice, destino):
        x = None
        if vertice.inicio.destino == destino:
            x = vertice.inicio.info
            vertice.inicio = vertice.inicio.siguiente
            vertice.tamanio -= 1
        else:
            ant = vertice.inicio
            act = vertice.inicio.siguiente
            while act is not None and act.destino != destino:
                ant = act
                act = act.siguiente
            if act is not None:
                x = act.info
                ant.siguiente = act.siguiente
                vertice.tamanio -= 1
            return x


    def eliminarVertice(self, info):
        x = None
        if self.inicio.info == info:
            x = self.inicio.info
            self.inicio = self.inicio.siguiente
            self.tamanio -= 1
        else:
            ant = self.inicio
            act = self.inicio.siguiente
            while act is not None and act.info != info:
                ant = act
                act = act.siguiente
            if act is not None:
                x = act.info
                ant.siguiente = act.siguiente
                self.tamanio -= 1
        if x is not None:
            aux = self.inicio
            while aux is not None:
                if aux.adyacentes.inicio is not None:
                    self.eliminarArista(aux.adyacentes, info)
                aux = aux.siguiente
        return x


    def get_tamanio(self):
        return self.tamanio


    def grafoVacio(self):
        return self.inicio is None


    def buscarVertice(self, info):
        aux = self.inicio
        while aux is not None and aux.info != info:
            aux = aux.siguiente
        return aux


    def buscarArista(vertice, info):
        aux = vertice.adyacentes.inicio
        while aux is not None and aux.info != info:
            aux = aux.siguiente
        return aux


    def existePaso(self, origen, destino):
        resultado = False
        if not origen.visitado:
            origen.visitado = True
            verticesAdyacentes = origen.adyacentes.inicio
            while verticesAdyacentes is not None and not resultado:
                adyacente = self.buscarVertice(verticesAdyacentes.destino)
                if adyacente.info == destino.info:
                    return True
                elif not adyacente.visitado:
                    resultado = self.existePaso(adyacente, destino)
                verticesAdyacentes = verticesAdyacentes.siguiente
        return resultado


    def adyacentes(self, vertice):
        aux = vertice.adyacentes.inicio
        while aux is not None:
            print(aux.destino, aux.info)
            aux = aux.siguiente


    def esAdyacente(vertice, destino):
        resultado = False
        aux = vertice.adyacentes.inicio
        while aux is not None and not resultado:
            if aux.destino == destino:
                resultado = True
            aux = aux.siguiente
        return resultado


    def marcarNoVisitado(self):
        aux = self.inicio
        while aux is not None:
            aux.visitado = False
            aux = aux.siguiente


    def imprimirVertices(self):
        aux = self.inicio
        while aux is not None:
            print(aux.info)
            aux = aux.siguiente


    def imprimirPorProfundidad(self, vertice):
        while vertice is not None:
            if not vertice.visitado:
                vertice.visitado = True
                print(vertice.info)
                adyacentes = vertice.adyacentes.inicio
                while adyacentes is not None:
                    adyacente = self.buscarVertice(adyacentes.destino)
                    if not adyacente.visitado:
                        self.imprimirPorProfundidad(adyacente)
                    adyacentes = adyacentes.siguiente
            vertice = vertice.siguiente


    def imprimirPorAmplitud(self, vertice):
        cola = Cola()
        while vertice is not None:
            if not vertice.visitado:
                vertice.visitado = True
                cola.arribo(vertice)
                while not cola.esVacia():
                    nodo = cola.atencion()
                    adyacentes = nodo.adyacentes.inicio
                    while adyacentes is not None:
                        adyacente = self.buscarVertice(adyacentes.destino)
                        if not adyacente.visitado:
                            adyacente.visitado = True
                            cola.arribo(adyacente)
                        adyacentes = adyacentes.siguiente
            vertice = vertice.siguiente


    def dijkstra(self, origen, destino):
        no_visitados = Heap(self.get_tamanio())
        camino = Pila()
        aux = self.inicio
        while aux is not None:
            if aux == origen:
                no_visitados.arribo([aux, None], 0)
            else:
                no_visitados.arribo([aux, None], inf)
            aux = aux.siguiente

        while not no_visitados.heap_vacio():
            dato = no_visitados.atencion()
            if dato[1][0] != origen:
                camino.apilar(dato)
            aux = dato[1][0].adyacentes.inicio
            while aux is not None:
                pos = no_visitados.busqueda_prioridad(self.buscarVertice(aux.destino))
                if no_visitados.vector[pos][0] > dato[0] + aux.info:
                    no_visitados.vector[pos][1][1] = dato[1][0]
                    no_visitados.cambiar_prioridad(pos, dato[0] + aux.info)
                aux = aux.siguiente

        #camino.imprimir()
        print("================================")
        camino.limpiar(origen, destino)
        camino.imprimir()
        return camino
