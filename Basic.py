a = int(input("Masukkan nilai a : "))
b = int(input("Masukkan nilai b : "))

c = a + b
d = a * b
e = a - b
f = a / b
print ("Hasil penjumlahan tersebut adalah :  ", c)
print ("Hasil perkalian tersebut adalah : ", d)
print ("Hasil pengurangan tersebut adalah : ", e)
print ("Hasil pembagian tersebut adalah : ", f)

print ("\n")

tulis = input ("Masukkan tulisan : ")
kata = input ("Masukkan batas pengulangan kata : ")

for x in range (int(0),int(kata)):
    print (tulis)
print ("\n")
i = 1
while (i<=100):
    print (i)
    i = i+1

print ("Menu makanan : 1. Bakso, 2. Nasgor, 3. Indomie")

pilih = input("Pilih menu : ")

if pilih==1:
    print ("Menu yang dipilih Bakso")
elif pilih==2:
    print ("Menu yang dipilih Nasgor")
elif pilih==3:
    print ("Menu yang dipilih Indomie")
    
