# Hello World by Python

print ("Hello World")

# Sintaks dan variabel

print (445)
print ("Harus bisa Python")
print ("vfeliciwa")
print ("yovita_15")
print ("Kafe Cimi Time Malang")
print (45567)

# sintaks dasar Profil

nama = "Habib Muzakki"
kelas = "12 Agama"
asal = "sumbar"
tinggi = "170 cm"
berat = "60 kg"

print ("Nama ", nama)
print ("Kelas :", kelas)
print ("Asal :", asal)
print ("Tinggi :", tinggi)
print ("Berat :", berat)

# sintaks dasar 2

k = "Belajar "
j = "di IBM SkillsBuild"

hasil = k + j
print (hasil)

a = "Belajar "
b = "Coding "
c = "di Bootcamp Indonesia"

hasil = a + b + c
print (hasil)

# tipe data

teks = "Halo Teks" # string
angka = 3445 # integer
des = 3.14 # float
li = ["vfeliciwa", "yovita_15", "Fun", "tes"] # list
ju = {"Set", "Hut", "dan", "Vot", "Dankut"} # Set
ko = ("Gujan", "Vest", "Roat", "Dankut", "Api") # Tuple

print (teks)
print (angka)
print (des)
print (li)
print (ju)
print (ko)

# operator dasar

x = 5
y = 4

print (x + y)
print (x - y)
print (x ** y)
print (x / y)
print (x % y)

# operator perbandingan

print (x > y)
print (x < y)
print (x == y)

# logika

print (x < y and x > y)
print (x > y or x < y)
print (not x)
print (not y)

# Tipe data Objek

dah = {
    "nama" : "Habib Muzakki Piliang",
    "kelas" : "12 Agama",
    "asal" : "Sumbar",
    "tinggi" : "170 cm",
    "berat" : "50 kg",
    "angkatan" : "34",
    "sekolah" : "MAN 2 Kota Serang",
} 

print ("Nama :", dah ["nama"])

print ("Kelas :", dah ["kelas"])

print ("Asal :", dah ["asal"])

print ("Tinggi :", dah ["tinggi"])

print ("Berat :", dah ["berat"])

print ("Angkatan :", dah ["angkatan"])

print ("Sekolah :", dah ["sekolah"])

print (dah)

# Percabangan dasar

t = 8

if t > 5:
    print ("Besar")
else:
    print ("Kecil")
    
# Percabangan lanjutan 

k = 4

if k > 5:
    print ("Kecil")
elif k < 5:
    print ("Besar")
else:
    print ("Semula")
    
# percabangan lanjutan 

l = 6

if l > 5:
    print ("5")
elif l == 4:
    print ("4")
elif l == 3:
    print ("3")
elif l == 2:
    print ("2")
elif l == 1:
    print ("1")
else:
    print ("semula")
    
# percabangan nested

c = 7

if c > 5:
    if (True):
        print ("Besar")
    elif c < 5:
        print ("Kecil")
else:
    print ("Semula")
    
# switch case

nilai = 8

match (nilai):
    
    case 8:
        print ("8")
    
    case 7:
        print ("7")
    
    case 6:
        print ("6")
        
    case 5:
        print ("5")
        
    case 4:
        print ("4")
        
    case 3:
        print ("3")
        
    case 2:
        print ("2")
        
    case 1:
        print ("1")
        
    case _:
        print ("Default")
    
# perulangan for 

for i in range (1, 6):
    print ("i", i)

for k in range (10, 15):
    print ("k", k)
    
for m in range (20, 26):
    print ("m", m)
    
# perulangan while

r = 5

while (r < 6):
    print ("r", r)
    r = r + r
    
t = 8

while (t < 10):
    print ("t", t)
    t = t + 1
    
m = 7

while (m < 15):
    print ("m", m)
    m = m + 1
    
    
# array

li = ["India", "Pakistan", "Jepang", "Indonesia"]

print (li)

for item in li:
    print (item)
    
ji = ["Jansen", "Mr Beast", "Felicia"]

print (ji)

for item in ji:
    print (item)
    
    
# objek 

deja = {
    "nama" : "Habib Muzakki Piliang",
    "kelas" : "12 Agama",
    "lomba" : "OSN Informatika",
    "asal" : "Sumbar",
    "tinggal" : "Kota Serang",
    "tinggi" : "170 cm",
    "berat" : "50 kg",
}

print ("Nama :", deja ["nama"]) 

print ("Kelas :", deja ["kelas"])

print ("Lomba :", deja ["lomba"])

print ("Asal :", deja ["asal"])

print ("Tinggal :", deja ["tinggal"])

print ("Tinggi :", deja ["tinggi"])

print ("Berat :", deja ["berat"])

print (deja)
    
# function utama

# tanpa parameter

def hujan ():
    print ("Hello World")
    
hujan ()
hujan ()

def kopling ():
    print ("halo Dunia")
    
kopling ()
kopling ()

def jiko ():
    print ("Halo anak Malang")
    
jiko ()
jiko ()
jiko ()

# dengan parameter

def sapa (nama):
    print ("Halo " + nama)
    
sapa ("Habib Muzakki")
sapa ("vfeliciwa")
sapa ("yovita_15")
sapa ("Kafe Cimi Time Malang")

def lomba (nama_lomba):
    print ("Saya ingin ikut lomba " + nama_lomba)
    
lomba ("OSN Informatika")
lomba ("Debat Bahasa Indonesia")
lomba ("MTQ")
lomba ("MHQ")

def mangu (nama):
    print ("Halo " + nama + " Cantik")
    
mangu ("vfeliciwa")
mangu ("yovita_15")
mangu ("aufa")
mangu ("aisyah")

def sekolah (nama_sekolah):
    print ("Saya sekolah di " + nama_sekolah)
    
sekolah ("MAN 2 Kota Serang")
sekolah ("SMPIT Al-Izzah Serang")
sekolah ("SDIT Al-Izzah Serang")

def mol (name):
    print ("Halo " + name + " semoga kamu menyenangkan")
    
mol ("Aufa")
mol ("Medina")
mol ("Naren")
mol ("Darel")
mol ("Gaza")

def juk (tes):
    print ("Halo " + tes + ", Kamu lagi apa")

juk ("Felicia")
juk ("Yovita")

# dengan return

def tambah (a, b):
    return a + b

hasil = tambah (10, 5)
print (hasil)

def kurang (x, y):
    return x - y

hasil = kurang (20, 8)
print (hasil)

def kali (m, n):
    return m * n

hasil = kali (5, 3)
print (hasil)