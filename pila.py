class nodoPila(object):
    info, siguiente = None, None


class Pila(object):
    def __init__(self):
        self.cima = None
        self.tamanio = 0


    def apilar(self, info):
        nuevoNodo = nodoPila()
        nuevoNodo.info = info
        nuevoNodo.siguiente = self.cima
        self.cima = nuevoNodo
        self.tamanio += 1


    def desapilar(self):
        info = self.cima.info
        self.cima = self.cima.siguiente
        self.tamanio -= 1
        return info


    def esVacia(self):
        return self.cima is None


    def imprimir(self):
        pilaAuxiliar = Pila()
        total = 0
        while not self.esVacia():
            info = self.desapilar()
            total += info[0]
            print(info[1][1].info,info[0], "h",info[1][0].info)
            pilaAuxiliar.apilar(info)
        while not pilaAuxiliar.esVacia():
            info = pilaAuxiliar.desapilar()
            self.apilar(info)

        print("Tiempo total de viaje:", total, "h")


    def enCima(self):
        if self.cima is not None:
            return self.cima.info
        else:
            return None


    def limpiar(self, origen, destino):
        pilaAuxiliar = Pila()
        while not self.esVacia():
            info = self.desapilar()
            if info[1][0] == destino or (info[1][0] == destino and info[1][1] == origen):
                pilaAuxiliar.apilar(info)
                destino = info[1][1]
        while not pilaAuxiliar.esVacia():
            info = pilaAuxiliar.desapilar()
            self.apilar(info)