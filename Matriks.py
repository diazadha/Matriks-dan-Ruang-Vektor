list1 = []
kolom = input("Masukkan kolom untuk matriks : ")
baris = input("Masukkan baris untuk matriks : ")

i = 0
while (i<int(kolom)):
    x = 0
    while (x<int(baris)):
        list1.append(input("A["+str(i)+"]["+str(x)+"] : "))
        x = x + 1
    i = i + 1
print ("\n")
print ("Hasil matriks tersebut adalah : ")
print ("\n")

d = 0
a = 1
while (a<=int(kolom)):
    print (list1[int(d):d+int(baris)])
    d = d + int(baris)
    a = a + 1






                                  
