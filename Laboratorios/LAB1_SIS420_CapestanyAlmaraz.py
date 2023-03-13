# Capestany Almaraz Luis Pablo
# SIS420     1/2023
# Laboratorio1
# Busqueda primero en anchura - Breadth First Search

class Nodo:
    def __init__(self, estado, hijo=None):
        self.estado = estado
        self.hijo = None
        self.padre = None
        self.accion = None
        self.acciones = None
        self.costo = None
        self.set_hijo(hijo)

    def set_estado(self, estado):
        self.estado = estado

    def get_estado(self):
        return self.estado

    def set_hijo(self, hijo):
        self.hijo = hijo
        if self.hijo is not None:
            for s in self.hijo:
                s.padre = self

    def get_hijo(self):
        return self.hijo
    
    def set_padre(self, padre):
        self.padre = padre

    def get_padre(self):
        return self.padre
    
    def set_accion(self, accion):
        self.accion = accion

    def get_accion(self):
        return self.accion

    def set_acciones(self, acciones):
        self.acciones = acciones

    def get_acciones(self):
        return self.acciones

    def set_costo(self, costo):
        self.costo = costo

    def get_costo(self):
        return self.costo

    def equal(self, Nodo):
        if self.get_estado() == Nodo.get_estado():
            return True
        else:
            return False

    def en_lista(self, lista_nodos):
        enlistado = False
        for n in lista_nodos:
            if self.equal(n):
                enlistado = True
        return enlistado

    def __str__(self):
        return str(self.get_estado())
    
def busqueda_BPA_solucion(estado_inicial, solucion):
    resuelto = False
    nodos_visitados = []
    nodos_frontera = []

    nodo_raiz = Nodo(estado_inicial)
    nodos_frontera.append(nodo_raiz)
    while (not resuelto) and len(nodos_frontera) != 0:
        nodo_actual = nodos_frontera.pop(0)
        # extraer nodo y añadirlo a visitados
        nodos_visitados.append(nodo_actual)
        if nodo_actual.get_estado() == solucion:
            # solucion encontrada
            resuelto = True
            return nodo_actual
        else:
            # expandir nodos hijo
            estado_nodo = nodo_actual.get_estado()

            # operador 1 (Accion uno, intercambiar la posicion 0 con la 1 del estado)
            # hijo = [estado_nodo[1], estado_nodo[0], estado_nodo[2], estado_nodo[3], estado_nodo[4], estado_nodo[5], estado_nodo[6], estado_nodo[7], estado_nodo[8], estado_nodo[9]]
            hijo = [estado_nodo[1], estado_nodo[0], estado_nodo[2], estado_nodo[3], estado_nodo[4],estado_nodo[5],estado_nodo[6],estado_nodo[7], estado_nodo[8], estado_nodo[9]]
            hijo_1 = Nodo(hijo)
            if not hijo_1.en_lista(nodos_visitados) and not hijo_1.en_lista(nodos_frontera):
                nodos_frontera.append(hijo_1)

            # operador 2 (Accion uno, intercambiar la posicion 1 con la 2 del estado)
            # hijo = [estado_nodo[0], estado_nodo[2], estado_nodo[1], estado_nodo[3], estado_nodo[4], estado_nodo[5], estado_nodo[6], estado_nodo[7], estado_nodo[8], estado_nodo[9]]
            hijo = [estado_nodo[0], estado_nodo[2], estado_nodo[1], estado_nodo[3],estado_nodo[4],estado_nodo[5],estado_nodo[6],estado_nodo[7], estado_nodo[8], estado_nodo[9] ]
            hijo_2 = Nodo(hijo)
            if not hijo_2.en_lista(nodos_visitados) and not hijo_2.en_lista(nodos_frontera):
                nodos_frontera.append(hijo_2)

            # operador 3 (Accion uno, intercambiar la posicion 2 con la 3 del estado)
            # hijo = [estado_nodo[0], estado_nodo[1], estado_nodo[3], estado_nodo[2], estado_nodo[4], estado_nodo[5], estado_nodo[6], estado_nodo[7], estado_nodo[8], estado_nodo[9]]
            hijo = [estado_nodo[0], estado_nodo[1], estado_nodo[3], estado_nodo[2], estado_nodo[4], estado_nodo[5],estado_nodo[6],estado_nodo[7], estado_nodo[8], estado_nodo[9]]
            hijo_3 = Nodo(hijo)
            if not hijo_3.en_lista(nodos_visitados) and not hijo_3.en_lista(nodos_frontera):
                nodos_frontera.append(hijo_3)

            # operador 4 (Accion uno, intercambiar la posicion 3 con la 4 del estado)
            # hijo = [estado_nodo[0], estado_nodo[1], estado_nodo[2], estado_nodo[4], estado_nodo[3], estado_nodo[5], estado_nodo[6], estado_nodo[7], estado_nodo[8], estado_nodo[9]]
            hijo = [estado_nodo[0], estado_nodo[1], estado_nodo[2], estado_nodo[4],estado_nodo[3],estado_nodo[5],estado_nodo[6],estado_nodo[7], estado_nodo[8], estado_nodo[9] ]
            hijo_4 = Nodo(hijo)
            if not hijo_4.en_lista(nodos_visitados) and not hijo_4.en_lista(nodos_frontera):
                nodos_frontera.append(hijo_4)

            # operador 5 (Accion uno, intercambiar la posicion 4 con la 5 del estado)
            # hijo = [estado_nodo[0], estado_nodo[1], estado_nodo[2], estado_nodo[3], estado_nodo[5], estado_nodo[4], estado_nodo[6], estado_nodo[7], estado_nodo[8], estado_nodo[9]]
            hijo = [estado_nodo[0], estado_nodo[1], estado_nodo[2], estado_nodo[3],estado_nodo[5],estado_nodo[4],estado_nodo[6],estado_nodo[7] , estado_nodo[8], estado_nodo[9] ]
            hijo_5 = Nodo(hijo)
            if not hijo_5.en_lista(nodos_visitados) and not hijo_5.en_lista(nodos_frontera):
                nodos_frontera.append(hijo_5)

             # operador 6 (Accion uno, intercambiar la posicion 5 con la 6 del estado)
            # hijo = [estado_nodo[0], estado_nodo[1], estado_nodo[2], estado_nodo[3], estado_nodo[4], estado_nodo[6], estado_nodo[5], estado_nodo[7], estado_nodo[8], estado_nodo[9]]
            hijo = [estado_nodo[0], estado_nodo[1], estado_nodo[2], estado_nodo[3],estado_nodo[4],estado_nodo[6],estado_nodo[5],estado_nodo[7], estado_nodo[8], estado_nodo[9]  ]
            hijo_6 = Nodo(hijo)
            if not hijo_6.en_lista(nodos_visitados) and not hijo_6.en_lista(nodos_frontera):
                nodos_frontera.append(hijo_6)

             # operador 7 (Accion uno, intercambiar la posicion 6 con la 7 del estado)
            # hijo = [estado_nodo[0], estado_nodo[1], estado_nodo[2], estado_nodo[3], estado_nodo[4], estado_nodo[5], estado_nodo[7], estado_nodo[6], estado_nodo[8], estado_nodo[9]]
            hijo = [estado_nodo[0], estado_nodo[1], estado_nodo[2], estado_nodo[3],estado_nodo[4],estado_nodo[5],estado_nodo[7], estado_nodo[6], estado_nodo[8], estado_nodo[9]]
            hijo_7 = Nodo(hijo)
            if not hijo_7.en_lista(nodos_visitados) and not hijo_7.en_lista(nodos_frontera):
                nodos_frontera.append(hijo_7)

            # operador 8 (Accion uno, intercambiar la posicion 7 con la 8 del estado)
            # hijo = [estado_nodo[0], estado_nodo[1], estado_nodo[2], estado_nodo[3], estado_nodo[4], estado_nodo[5], estado_nodo[6], estado_nodo[8], estado_nodo[7], estado_nodo[9]]
            hijo = [estado_nodo[0], estado_nodo[1], estado_nodo[2], estado_nodo[3],estado_nodo[4],estado_nodo[5],estado_nodo[6], estado_nodo[8], estado_nodo[7], estado_nodo[9]]
            hijo_8 = Nodo(hijo)
            if not hijo_8.en_lista(nodos_visitados) and not hijo_8.en_lista(nodos_frontera):
                nodos_frontera.append(hijo_8)

            # operador 9 (Accion uno, intercambiar la posicion 8 con la 9 del estado)
            # hijo = [estado_nodo[0], estado_nodo[1], estado_nodo[2], estado_nodo[3], estado_nodo[4], estado_nodo[5], estado_nodo[6], estado_nodo[7], estado_nodo[9], estado_nodo[8]]
            hijo = [estado_nodo[0], estado_nodo[1], estado_nodo[2], estado_nodo[3],estado_nodo[4],estado_nodo[5],estado_nodo[6], estado_nodo[7], estado_nodo[9], estado_nodo[8]]
            hijo_9 = Nodo(hijo)
            if not hijo_9.en_lista(nodos_visitados) and not hijo_9.en_lista(nodos_frontera):
                nodos_frontera.append(hijo_9)

            # operador 4
            # hijo = [estado_nodo[0], estado_nodo[1], estado_nodo[2], estado_nodo[4], estado_nodo[3]]
            # hijo_4 = Nodo(hijo)
            # if not hijo_4.en_lista(nodos_visitados) and not hijo_4.en_lista(nodos_frontera):
            #     nodos_frontera.append(hijo_4)


            # nodo_actual.set_hijo([hijo_1, hijo_2, hijo_3, hijo_4])
            nodo_actual.set_hijo([hijo_1, hijo_2, hijo_3, hijo_4, hijo_5, hijo_6, hijo_7, hijo_8, hijo_9] )


if __name__ == "__main__":
    #estado_inicial = [0,1,2,3,4,5,6,7,8,9]
    #solucion = [0,1,2,3,4,5,6,7,9,8]
    estado_inicial = [0, 1, 2, 3,4, 5,6,7, 9, 8]
    solucion = [0, 1, 2,3,4,5,7,6, 8, 9]
    nodo_solucion = busqueda_BPA_solucion(estado_inicial, solucion)
    # mostrar resultado
    resultado = []
    nodo_actual = nodo_solucion
    while nodo_actual.get_padre() is not None:
        resultado.append(nodo_actual.get_estado())
        nodo_actual = nodo_actual.get_padre()

    resultado.append(estado_inicial)
    resultado.reverse()
    print(resultado)