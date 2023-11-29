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
    while not self.esVacia():
        info = self.desapilar()
        print(info[1][0].info,info[0],info[1][1] )
        pilaAuxiliar.apilar(info)
    while not pilaAuxiliar.esVacia():
        info = pilaAuxiliar.desapilar()
        self.apilar(info)


def enCima(self):
    if self.cima is not None:
        return self.cima.info
    else:
        return None