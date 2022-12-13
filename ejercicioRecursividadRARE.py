def contarLista(lista):
    if len(lista)<=0:
        return 0
    return contarLista(lista[1:]) + lista[0]
    
lista = []
while True:
    num = input("Introduzca numero @ para parar: ")
    if num == "@":
        break
    elif num !="@":
        lista.append(int(num))
suma = int(input("Suma de la lista?: "))
if contarLista(lista) == suma:
    print("La suma es correcta...")
else:
    print("La suma NO se corresponde...")
    print(contarLista(lista))