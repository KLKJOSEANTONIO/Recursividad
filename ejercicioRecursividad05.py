def comparaLista(lista1,lista2):
    if len(lista1)==1:
        return lista1[0]
    if len(lista2)==0:
        return lista2[0]
    if len(lista2)!=len(lista1):
        return False
    if lista1[0]==lista2[0]:
        return True
    if lista1[0]!=lista2[0]:
        return False
    return comparaLista(lista1[1:],lista2[1:])

lista1=[3,4,7]
lista2=[3,4,7]

print("Primeras listas...")
if comparaLista(lista1,lista2):
    print("SI")
else:
    print("NO")
lista1=[3,4,7]
lista2=[7,4,7]

print("SEGUNDAS listas...")
if comparaLista(lista1,lista2):
    print("SI")
else:
    print("NO")
    
lista1=[3,4,7,6]
lista2=[3,4,7]
print("TERCERA listas...")
if comparaLista(lista1,lista2):
    print("SI")
else:
    print("NO")


#FINALIZADO