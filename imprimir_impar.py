lista=[1,2,3,4,5]



# while True:
#     try:
#         for i in range(len(lista)):
#             print(lista[i])
#             lista.pop(i)
#         break
#     except IndexError:
#         pass

def listaPares(auxlista):
    try:
        for i in range(len(lista)):
            print(lista[i])
            lista.pop(i)
    except IndexError:
        pass
