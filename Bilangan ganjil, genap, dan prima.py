def ganjil(banyak):
    i = 1
    b = 1
    while (i<=banyak):
        print ("", b, end = "")
        b = b + 2
        i = i + 1
    return b

def genap(banyak):
    i = 1
    b = 0
    while (i<=banyak):
        print ("", b, end = "")
        b = b + 2
        i = i + 1
    return b

def prima(p):
    i = 1
    prim = 2
    while (i<=p-1):
        for x in range (2, prim):
            if (prim % x == 0):
                break
        else:
            print ("", prim, end = "")
        prim = prim + 1
        i = i + 1
    return prim

N = int(input("Banyaknya bilangan ganjil : "))
ganjil(N)

banyak = int(input("\nBanyaknya bilangan genap : "))
genap(banyak)

p = int(input("\nBatas atas dari deret bilangan prima : "))
prima(p)
