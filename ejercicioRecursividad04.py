#voltear un string
def palabra(pal):
    if len(pal)==0:
        return pal
    return pal[-1]+palabra(pal[:-1])
print(palabra("hola"))