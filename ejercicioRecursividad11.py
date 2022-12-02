#palindromo recursivo
def palindromo(n):
    if len(n)==0:
        return n
    volteada = n[-1]+palindromo(n[:-1])
    if len(volteada) == len(n) and len(n)!=0:
        if volteada == n:
            return True
        else:
            return n
    else:
        return n
n = "libra"
print(palindromo(n))