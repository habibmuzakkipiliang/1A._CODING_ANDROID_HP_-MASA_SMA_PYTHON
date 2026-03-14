# hello world Python

print ("Hello World","\n")

# string dasar Python

teks = "Semangat belajar coding Python"

print (teks. upper ()) # semua huruf besar
print (teks. lower ()) # semua huruf kecil
print (teks. title ()) # judul nya
print (teks. swapcase ()) # tukar huruf kecil ke besar dan huruf besar ke kecil
print (teks. capitalize ()) # huruf pertama jadi huruf kapital
print (teks. replace ("Python", "HTML")) # ganti kata jadi kata baru
print (teks. strip ()) # menghapus spasi di awal dan akhir
print ("Python" in teks, "\n") # dalam Teks kode itu


# variabel Python

a = "Halo Aku Habib Muzakki "
b = "Lagi belajar Bahasa Pemrograman Python "
c = "dan jangan lupa selalu semangat ya "

hasil = a + b + c
print (hasil, "\n")

# tipe data Python

angka = 12 # integer
desimal = 3.14 # float
string = "Halo dunia" # String
hook = True # boolean
daf = ["Lishani", "Lailan", "Farha", "Nadya"] # list
tup = ("Indonesia", "Malaysia", "Brunei") # tuple
det = {"Hayyan", "Hanif", "Dudun", "Edi"} # set

print ("Integer : ", angka)
print ("Float : ", desimal)
print ("String : ", string)
print ("Boolean : ", hook)
print ("List : ", daf)
print ("Tuple : ", tup)
print ("Set : ", det, "\n")

# operator arimatika Python

a = 10
b = 4

print ("Tambah = ", a + b)
print ("Kurang = ", a - b)
print ("Kali : ", a * b)
print ("Pangkat : ", a ** b)
print ("Pembagian : ", a / b)
print ("Pembagian bulat", a // b)
print ("Modulus : ", a % b, "\n")

# operator perbandingan Python

x = 90
y = 89

print ("Hasilnya : ", x > y)
print ("Hasilnya : ", x < y)
print ("Hasilnya :", x == y)
print ("Hasilnya : ", x <= y)
print ("Hasilnya : ", x >= y)
print ("Hasilnya : ", x != y, "\n")

# operator logika Python

k = 45
j = 40

print ("Hasilnya : ", k > j and k < j)
print ("Hasilnya : ", k < j or k > j)
print ("Hasilnya : ", not (k < j))
print ("Hasilnya : ", not (k > j), "\n")

# Percabangan Python

a = 50

if a > 50 :
    print ("Besar")
elif a < 50 :
    print ("Kecil")
else :
    print ("Sama saja")
    
# for perulangan Python

a = 1

for a in range (1, 5):
    print (a)
    
b = 5

for b in range (6, 8):
    if b == 5:
        continue
    print (b)
    
# Function def Python

def sapa_anda ():
    print ("Hello Nadia Sukmanang")

sapa_anda ()
sapa_anda ()

def sapa_aku (sapa_aku):
    print ("Halo " + sapa_aku)

sapa_aku ("Pinkan Nadia")
sapa_aku ("Nadira")

def tambah (a, u):
    return a + u

hasil = tambah (2, 5)
print (hasil)

def kurang (u, i):
    return u - i

hasil = kurang (100, 50)
print (hasil)