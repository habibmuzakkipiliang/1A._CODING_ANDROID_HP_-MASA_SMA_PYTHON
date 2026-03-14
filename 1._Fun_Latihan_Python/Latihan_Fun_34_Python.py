# Hello World by Python

print ("Halo Dunia by Python")

# sintaks dasar Python

print ("Kafe Cimi Time Malang")
print ("Felicia Kurniawati")
print ("vfeliciwa")
print ("IBM SkillsBuild")
print ("M. Wisnu Haris")
print ("Semangat Belajarnya")
print ("Alfitra Rizky Ramadhan")
print ("Halo Justinian")
print ("Halo Pedro Alfinian")
print ("Determinan")
print ("Hasta Muerte")
print ("Halo Filza Gibran")
print ("Halo Berlin")
print ("Halo Oslo")
print ("Halo Kopenhagen")

a = "Halo "
b = "Internasional "
hasil = a + b
print (hasil)

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

x = 22
y = 2

print (x + y)
print (x - y)
print (x ** y)
print (x * y)
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

t = "Duri Jansen"
r = 23
j = 3.14
q = True
k = ["Duri", "Sam", "Fur"]
o = {"Fur", "Zan", "Rez"}

print (r)
print (r)
print (j)
print (k)
print (o)

# percabangan dasar

h = 20

if h < 19:
    print ("Besar")
else: 
    print ("Kecil")
    

# percabangan lanjutan

g = 30

if g > 23:
    print ("Besar")
elif g < 50:
    print ("Kecil")
else:
    print ("Sama saja")
    
j = 100

if g == 100:
    print ("Bagus")
elif g == 90:
    print ("Oke")
elif g == 80:
    print ("Mantap jiwa")
elif g == 75:
    print ("di bawah kkm")
elif g == 70:
    print ("Remedial")
else:
    print ("Sama saja")
    
# percabangan nested

r = 12

if r < 30:
    if (True):
        print ("Besar")
    elif r > 30:
        print ("Kecil")
else:
    print ("Sama")
    
# switch Python

e = 5

match (e):
    
    case 1:
        print ("Nilai kecil")
        
    case 2:
        print ("Nilai agak kecil")
        
    case 3:
        print ("Sedang")
        
    case 4:
        print ("Agak Besar")
        
    case 5:
        print ("Sangat besar")
        
    case _:
        print ("Sama saja")
        
# perulangan for

for v in range (1,6):
    print ("For", v)
    
for h in range (0, 10):
    print ("Dri", h)
    
for q in range (6, 10):
    print ("Yard", q)
    
for j in range (11, 15):
    print ("Dart", j)

for u in range (1,6):
    if u == 4:
        break
    print ("Lab", u)
    
for q in range (1,6):
    if q == 3:
        continue
    print ("Las", q)
    
# perulangan while

w = 0

while (w < 3):
    print ("While", w)
    w = w + 1
    
d = 0

while (d < 6):
    print ("Qhure", d)
    d = d + 1
    
j = 0

while (j < 7):
    print ("h ke", j)
    j = j + 1
    
k = 0
while (k < 10):
    print ("k", k)
    k = k + 1
    
# data Array dan object

ang = ["Liberte", "Sanday", "Object", "Drainase"]

print (ang)

dic = {
    "nama" : "Habib Muzakki",
    "kelas" : "12",
    "tinggi" : "172 cm",
    "berat" : "61 kg",
}

print ("Nama :", dic ["nama"])
print ("Kelas :", dic ["kelas"])
print ("Tinggi :", dic ["tinggi"])
print ("Berat :", dic ["berat"])

# function def

def ras ():
    print ("Selamat Hari")
    
ras ()
ras ()
ras ()
ras ()


def rat ():
    print ("Hasla Huj")
    print ("Espanol")
    print ("Rater")
    
rat ()


def wer ():
    print ("Hayyan Faras")
    print ("Ascendria")
    print ("Soft")
    print ("Yard")
    
wer ()

def rut ():
    print ("Hasta Munjer")

rut ()
rut ()
rut ()


def tambah (z,n):
    return z + n
    
hasil = tambah (1, 3)
print (hasil)


def kurang (a, b):
    return a - b
    
hasil = kurang (2, 3)
print (hasil)

def bagi (t, h):
    return t / h
    
hasil = bagi (12, 2)
print (hasil)
