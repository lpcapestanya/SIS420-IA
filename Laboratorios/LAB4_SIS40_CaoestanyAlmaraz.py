# Estado inicial
estado_inicial = r' /\\\n/\\/\\\n / \\'

# Estado objetivo
estado_objetivo = r" /\
/\/\
 / "

# Función para generar los posibles movimientos a partir de un estado dado
def generar_movimientos(estado):
    movimientos = []
    for i in range(len(estado)-1):
        for j in range(i+1, len(estado)):
            if estado[i:i+2] != r"\/" and estado[i:i+2] != r"/\\":
                nuevo_estado = estado[:i] + r"\/" + estado[i+2:j] + r"/\\" + estado[j+2:]
                movimientos.append(nuevo_estado)
    return movimientos

# Función de búsqueda en profundidad recursiva
def busqueda_profundidad(estado_actual, visitados):
    if estado_actual == estado_objetivo:
        return []
    visitados.append(estado_actual)
    movimientos = generar_movimientos(estado_actual)
    for nuevo_estado in movimientos:
        if nuevo_estado not in visitados:
            solucion = busqueda_profundidad(nuevo_estado, visitados)
            if solucion is not None:
                return [(estado_actual, nuevo_estado)] + solucion
    return None

# Llamada inicial a la función de búsqueda en profundidad
solucion = busqueda_profundidad(estado_inicial, [])
if solucion is None:
    print("No se encontró solución.")
else:
    print("Secuencia de movimientos:")
    for mov in solucion:
        print(mov[0])
    print(estado_objetivo)
