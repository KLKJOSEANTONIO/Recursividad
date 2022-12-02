#SUMAR LISTA
def sumarLista(lista):
    if len(lista)<=0:
        return 0
    return sumarLista(lista[1:]) + lista[0]
lista = [1,20,3,4,50]
print(sumarLista(lista))