#palindromo recursivo
def palindromo(n):
    if len(n)==0:
        return n
    volteada = n[-1]+palindromo(n[:-1])
    return n == volteada
n = "libra"
print(palindromo(n))