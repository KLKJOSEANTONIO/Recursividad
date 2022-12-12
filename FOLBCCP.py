def sumarLista(lista):
    if len(lista)<=0:
        return 0
    return sumarLista(lista[1:]) + lista[0]
bccp=[]

salario_base=float(input("Introduzca el salario base: "))
cant_pagas = input("Cuantas pagas extras?: ")
pagas_extras = float(input("Introduzca cantidad paga extra: "))
if cant_pagas ==2 or cant_pagas=="2":
    pagas_extras = float(pagas_extras*2/12)
bccp.append(salario_base)
bccp.append(pagas_extras)
hay_porcentual=input("hay complemento en porcentaje?: ")
if hay_porcentual=="si" or hay_porcentual=="Si":
    porcentaje=float(input("Introduzca el porcentaje: "))
    cantidad = float(input("Cantidad del porcentaje: "))
    cada_cuanto=float(input("Cada cuantos año es el beneficio: "))
    años_en_empresa=float(input("Cuantos años llevas en la empresa: "))
    años_de_beneficio=años_en_empresa//cada_cuanto
    porcentaje_total=(cantidad*porcentaje/100)*años_de_beneficio
hay_complementos_salariales = input("Hay complementops salariales?: ")
if hay_complementos_salariales == "Si" or hay_complementos_salariales == "si" or hay_complementos_salariales == "SI":
    while True:
        complementos_salariales = input("Introduzca complemento para parar :@ ")
        if complementos_salariales=="@":
            break
        else:
            bccp.append(float(complementos_salariales))
print(sumarLista(bccp))