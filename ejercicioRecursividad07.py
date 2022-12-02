#minimo lista
def minimoLista(lista):
    if len(lista) ==1:
        return lista[0]
    siguiente = minimoLista(lista[1:])
    if lista[0]<=siguiente:
        return lista[0]
    else:
        return siguiente
lista = [2,9,3,45,17,4]
print(minimoLista(lista))
#FINALIZADO