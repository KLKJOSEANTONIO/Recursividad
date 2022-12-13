def f(x):
    a=0
    while a!=1000:
        a+=1
        yield a

a=f(5)

while True:
    try:
        print(next (a))
    except StopIteration:
        print("lmao nig")