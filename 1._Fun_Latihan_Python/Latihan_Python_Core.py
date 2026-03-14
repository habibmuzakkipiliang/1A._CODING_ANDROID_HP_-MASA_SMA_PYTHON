# Hello World Python

print ("Hello World")




# sintaks dasar Python

teks = "Halo Teks"
print (teks)

angka = 34
print (angka)

desimal = 3.14
print (desimal)



# Sintaks dasar opsi

print ("Halo Dunia MAN 2")

print ("Halo Dunia Kuliah")

print ("Halo Baraju")



# Sintaks dasar 2

ini_text = "Soft File"
ini_angka = 345
ini_desimal = 3.14
ini_bool = True
ini_char = 'A'

print (ini_text)
print (ini_angka)
print (ini_desimal)
print (ini_bool)
print (ini_char)



# sintaks dasar 2 Python

nama = "Habib Muzakki"
umur = 20
koma = 4.56

print ("Nama :", nama)
print ("Umur :", umur)
print ("Koma :", koma)


# sintaks dasar 3 Python 

a = "- Halo "
b = "Claire Shane Ailie Sumantri, "
c = "Cantik dan Keren, "
d = "Karena ikut dan berhasil juara OSN Informatika 2025"
	
hasil = a + b + c + d
	
print (hasil)




# sintaks dasar 4 Python
	
x = "- Halo "
z = "Joanne Henrietta Fajar, "
w = "Semangat ya Cantik "
	
hasil_4 = x + z + w

print (hasil_4)


	
	
# sintaks dasar 4 Python
	
v = "- Halo Felicia Kurniawati, "
t = "kamu sangat cantik dan ceria dan pemilik Cimi Timi Cafe Malang, "
e = "dan kamu itu sangat manis "
	
hasil_5 = v + t + e
	
print (hasil_5)




# sintaks dasar 5 Python

gk = "- Halo Kezia Samantha, "
ko = "kamu adalah seorang Influencer terkenal dari Surabaya, "
ml = "dan kamu itu sangat manis "

hasil_6 = gk + ko + ml

print (hasil_6)




# operasi dasar Python

a = 10
b = 5

print ("Penjumlahan:", a + b)
print ("Pengurangan:", a - b)
print ("Perkalian:", a * b)
print ("Pembagian:", a / b)
print ("Modulus:", a % b)
print ("Pangkat:", a ** b)
print ("Pembagian Bulat:", a // b)




# operator perbandingan Python

print ("Sama dengan:", a == b)
print ("Tidak sama dengan:", a != b)
print ("Lebih besar dari:", a > b)
print ("Lebih kecil dari:", a < b)




# operator logika Python

print ("Dan:", (a > b) and (b > 0))
print ("Atau:", (a > b) or (b < 0))
print ("Tidak:", not (a > b))




# tipe data dasar Python

teks = "Belajar Python"
angka = 42
desimal = 3.14159
boolean = True
daftar = [1, 2, 3, 4, 5]
tuple_data = (10, 20, 30)
kamus = {"nama": "Andi", "umur": 25}
set_data = {1, 2, 3, 4, 5}

print (teks)
print (angka)
print (desimal)
print (boolean)
print (daftar)
print (tuple_data)
print (kamus)
print (set_data)




# percabangan dasar

nilai = 75

if nilai > 85:
    print ("Nilai Anda A")
    
else:
    print ("Nilai Anda C")
    
 
 
    
# percabangan lanjutan

nilai_kop = 90

if nilai_kop > 85:
    print ("Nilai Anda A")

elif nilai_kop > 70:
    print ("Nilai Anda B")
    
elif nilai_kop > 60:
    print ("Nilai Anda C")

elif nilai_kop > 50:
    print ("Nilai Anda D")

else:
    print ("Nilai Anda E")
 
 
    
    
# percabangan bersarang (nested)

nilai_akhir = 65

if nilai_akhir > 60:
    if (True):
        print ("Selamat, Anda Lulus!")
    
    elif nilai_akhir > 80:
        print ("Nilai Anda A")
    
    elif nilai_akhir > 70:
        print ("Nilai Anda B")
    
else:
    print ("Nilai Anda C")
 
 
        
        
# perulangan for

for i in range (5):
    print ("i", i)
    
    
for w in range (1, 5):
    print ("w", w)
    
    
for k in range (1, 10):
    print ("k", k)
    
    
for l in range (10, 20):
    print ("l", l)
    
    
for t in range (11, 20):
    print ("t", t)
    
    
for gh in range (45):
    print ("gh", gh)


    
    
# perulangan while 

count = 5
while count < 5:
    print ("Count :", count)
    count = count + 1
    
    
    
counte = 5
while counte < 5:
    print ("Counte :", counte)
    count = counte + 1
    
    
    
joki = 6
while joki < 6:
    print ("Joki", joki)
    joki = joki + 1
    
    

kolo = 4
while kolo < 4:
    print ("Kolo", kolo)
    kolo = kolo + 1
    
    
    
hulu = 6
while hulu < 6:
    print ("hulu", hulu)
    hulu = hulu + 1
    
    
    
say = 5
while say < 5:
    print ("say", say)
    say = say + 1
    
 
 
    
# match case

hari = 3

match (hari):
    
    case 1:
        print ("Senin")
        
    case 2:
        print ("Selasa")
        
    case 3:
        print ("Rabu")
        
    case 4:
        print ("Kamis")
        
    case 5:
        print ("Jumat")
        
    case 6:
        print ("Sabtu")
        
    case 7:
        print ("Minggu")
        
    case _:
        print ("Hari tidak valid")



        
# Array

buah = ["apel", "pisang", "jeruk"]
print (buah)



lor = ["mobil", "motor", "sepeda"]
print (lor)



fon = ["samsung", "iphone", "xiaomi"]
print (fon)



rt = ["Cimi", "Mbok To", "Chipi", "Taka"]
print (rt)



ko = ["Jerman", "Inggris", "Jepang", "Tiongkok"]
print (ko)




# Dictionary

data = {
    "nama": "Budi",
    "umur": "30 Tahun",
    "kota": "Jakarta",
    "pekerjaan" : "Programmer", 
}

print ("Nama :", data ["nama"])

print ("Umur :", data ["umur"])

print ("Kota :", data ["kota"])

print ("Pekerjaan :", data ["pekerjaan"])

print (data)




# Fungsi dasar

def sapa ():
    print ("Halo, Selamat Datang!")

sapa ()



def kop ():
    print ("Halo, Selamat Pagi!")
    
kop ()
kop ()
kop ()
kop ()



def pik ():
    print ("Janson")
    print ("Hello K")
    print ("Daftar")
    
pik ()

        

# Fungsi dengan parameter

def ton (nama):
    print ("Halo " + nama + ", Selamat datang di CCIT-FTUI")

ton ("Habib")
ton ("Rayyan")
ton ("Hayyan")
ton ("Dio")



def sapa_1 (nama):   
    print ("Halo " + nama + ", Cantik dan manis ")
    
sapa_1 ("Claire")
sapa_1 ("Dina")
sapa_1 ("Eva")
sapa_1 ("Fiona")



def sapa_2 (name):
    print ("Halo " + name + ", Selamat datang di Jakarta ")

sapa_2 ("Charlie")
sapa_2 ("Halim")



def jiko (name): 
    print ("Halo " + name + ", Cantik banget kamu ya sayang ")
    
jiko ("Christy")
jiko ("Olla")
jiko ("Freya")
jiko ("Gracia")
jiko ("Shani")



def har (nama):
    print ("Halo " + nama + ", Asal dari Jakarta Pusat")
    
har ("Rayhan")
har ("Rayyan")
har ("Faris")
har ("Hayyan")
har ("Ditan")
har ("Fakhri")



def jao (fes):
    print ("Tes " + fes + ", Alat baru aku")
    
jao ("janse")
jao ("Tae")
jao ("Fau")
jao ("Interger")




# fungsi dengan return

def tambah (a, b):
    return a + b

hasil = 2, 6
print (hasil)



def kurang (x, y ):
    return x - y

hasil = 10, 5
print (hasil)



def kali (y, k):
    return y * k

hasil = 10, 10
print (hasil)



def bagi (e, w):
    return e / w

hasil = 10, 5
print (hasil)



def bagi_bulat (p, w):
    return p // w

hasil = 56, 45
print (hasil)