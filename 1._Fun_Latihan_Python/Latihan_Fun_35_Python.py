# Hello World by Python

print ("Hello World by Python")

# Sintaks dasar Python

print ("Kafe Cimi Time Malang")
print ("Felicia Kurniawati")
print ("vfeliciwa")
print ("Tailwind")
print ("IBM SkillsBuild")
print ("Tabing")
print ("BIM")
print ("Era Modern")
print ("Era Terbaik")

e = "Jensen "
k = "Huang "
j = "Ceo "
b = "dari Nvdia "
h = "Internasional "
hasil = e + k + j + b + h
print (hasil)

print (12.4)
print (12)
print (3.14)
print (34.45)
print (56.34)
print (2.12)

# operator Python

x = 10
y = 5

print (x + y)
print (x - y)
print (x * y)
print (x ** y)
print (x / y)
print (x // y)
print (x % y)

print (x > y)
print (x < y)
print (x == y)

print (x > y and x < y)
print (x < y or x > y)
print (not x)
print (not y)

# tipe data Python

r = "Text ini "
k = 3.14
h = 23
b = True
l = ["Tes", "Ikon", "False"]
o = {"Fur", "Set", "Ilon"}

print (r)
print (k)
print (h)
print (k)
print (b)
print (l)
print (o)

# Percabangan dasar

r = 3

if r < 5:
    print ("Besar")
else:
    print ("Sama saja")
    
# percabangan lanjutan

h = 5

if h > 4:
    print ("Kecil")
elif h < 6:
    print ("Besar") 
else:
    print ("Sama saja")
    
j = 100

if j == 100:
    print ("A")
elif j == 95:
    print ("B")
elif j == 90:
    print ("C")
elif j == 85:
    print ("D")
elif j == 80:
    print ("E")
elif j == 75:
    print ("F")
elif j == 70:
    print ("G")
else:
    print ("Default")
    
# percabangan nested

a = 7

if a < 5:
    if (True):
        print ("Besar")
    elif a > 5:
        print ("Kecil")
else:
    print ("Sama saja")
    
# Switch

l = 3

match (l):
    
    case 1:
        print ("awal")
        
    case 2:
        print ("awal 1")
        
    case 3:
        print ("Tengah")
        
    case 4:
        print ("akhir 1")
        
    case 5:
        print ("akhir 2")
        
    case _:
        print ("Default")
        
# for perulangan

for i in range (0, 6):
    print ("i", i)
    
for q in range (0, 7):
    print ("q", q)
    
for w in range (0, 8):
    print ("w", w)
    
for y in range (0, 9):
    print ("y", y)
    
for x in range (0, 10):
    if x == 5:
        break
    print ("X", x)
    
for w in range (0, 10):
    if w == 3:
        continue
    print ("W", w)
    
# while

e = 0

while (w < 5):
    print ("W", e)
    e = e + 1
    
j = 0

while (j < 10):
    print ("H ", j)
    j = j + 1
    
k = 0

while (k < 10):
    print ("K", k)
    k = k + 1
    
j = 0 
while (j < 10):
    print ("J", j)
    j = j + 1
    
# data array dan objectl

huj = ["Felicia", "Cimi", "Malang", "Jatim"]

print (huj)

ob = {
    "nama" : "Habib Muzakki",
    "kelas" : "12 Agama",
    "tinggi" : "170 cm",
    "berat" : "60 kg",
    "darah" : "B",
}

print ("Nama :", ob ["nama"])
print ("Kelas :", ob ["kelas"])
print ("Tinggi :", ob ["tinggi"])
print ("Berat : ", ob ["berat"])
print ("Darah :", ob ["darah"])

# function Python

def halo ():
    print ("Halo Dunia")
    
halo ()
halo ()
halo ()
halo ()
halo ()


def yuin ():
    print ("Halo John")
    print ("Halo Trans")
    print ("Halo Frans")
    print ("Halo Unit 301")
    
yuin ()

def tambah (a, b):
    return a + b
    
hasil = tambah (10, 20)
print (hasil)


def kurang (r, t):
    return r - t
    
hasil = kurang (34, 30)
print (hasil)

def kali (r, k):
    return r * k
    
hasil = kali (10, 10)
print (hasil)