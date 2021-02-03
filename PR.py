def luas_persegi_panjang(panjang_persegi_panjang,lebar_persegi_panjang):
    return (panjang_persegi_panjang * lebar_persegi_panjang)
def keliling_persegi_panjang(panjang_persegi_panjang,lebar_persegi_panjang):
    return 2 * (panjang_persegi_panjang + lebar_persegi_panjang)

def luas_lingkaran(jari):
    return 3.14 * jari * jari
def keliling_lingkaran(jari):
    return 2 * 3.14 * jari

def luas_segitiga(a,t):
    return (a * t) / 2
def keliling_segitiga(a,b,c):
    return a + b + c

print ("""Pilihan Bangun :
1. Persegi panjang
2. Lingkaran
3. Segitiga""")

print ("\n")

pilih = int(input("Silahkan pilih nomor bangun diatas untuk dihitung luas & kelilingnya : "))

print ("\n")

if pilih==1:
    panjang = float(input("Masukkan panjang persegi panjang : "))
    lebar = float(input("Masukkan lebar persegi panjang : "))
    print ("Luas persegi panjang :", luas_persegi_panjang(panjang,lebar))
    print ("Keliling persegi panjang : ", keliling_persegi_panjang(panjang,lebar))
elif pilih==2:
    r = float(input("Masukkan jari - jari lingkaran : "))
    print ("Luas lingkaran : ", luas_lingkaran(r))
    print ("Kelliling lingkaran : ", keliling_lingkaran(r))
else:
    alas = float(input("Masukkan alas segitiga : "))
    tinggi = float(input("Masukkan tinggi segitiga : "))
    print ("Luas segitiga : ", luas_segitiga(alas,tinggi))
    print ("Sisi 1 segitiga = ", alas)
    print ("Silahakan masukkan 2 sisi berikutnya untuk menghitung keliling : ")
    sisi2 = float(input("Masukkan sisi 2 segitiga : "))
    sisi3 = float(input("Masukkan sisi 3 segitiga : "))
    print ("Keliling segitiga : ", keliling_segitiga(alas,sisi2,sisi3))
           
        
