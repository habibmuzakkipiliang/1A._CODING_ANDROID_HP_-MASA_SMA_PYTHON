# Hello World

print ("Hello World by Python")

# sintaks dasar dan variabel

a = "Napoleon Bonaparte "
print (a)

b = 12 
print (b)

c = 3.12 
print (c)

# tambahkan bonus

wool = "Belajar "
write = "Coding "
guji = "JavaScript "
koor = "dan Python "
nool = "dengan semangat "

hasil = wool + write + guji + koor + nool

print (hasil)

# operator dasar

x = 13
y = 3

print ("Tambah :", x + y)
print ("Kali : ", x * y)
print ("Pangkat : ", x ** y)
print ("Bagi : ", x / y)
print ("Bagi double : ", x // y)
print ("Modulus : ", x % y)
print ("Kurang : ", x - y)


# Operator perbandingan

print ("Hasilnya : ", x > y)
print ("Hasilnya : ", x < y)
print ("Hasilnya : ", x == y)
print ("Hasilnya : ", x <= y)
print ("Hasilnya : ", x >= y)

# operator logika

e = True
r = False

print (e < r and e > r)
print (e > r or e < r)
print (not r)
print (not e)


# percabangan biasa 

r = 23

if r > 12:
    print ("Besar")
elif r < 50:
    print ("Kecil")
else:
    print ("Sama saja")
    
# percabangan nested 

v = 50
cek = True

if v < 23:
    if (cek == True):
        print ("Besar")
    elif v > 23:
        print ("Kecil")
else:
    print ("Sama saja")
    
# for perulangan dan variasinya 

for i in range (1,5):
    print ("Range ke ", i)
    
for a in range (6,8):
    if a == True:
        continue
    print ("Tes :", a)
    
for t in range (8,10):
    if t == False:
        break
    print ("Gui", t)
    
    
li = ["Carlo", "Rudi", "Carlius", "Jansen"]

for item in li:
    print (item)
    
for item in li:
    print (li)
    
for item in sorted (li):
    print (item)
    
# perulangan while


r = 0

while (r < 5):
    print ("Halo ke - ", r)
    r = r + 1
    
j = 0

while (j < 10):
    print ("H ke -", j)
    j = j + 1
    
    
k = 10

while (k < 3):
    print ("J Ke - ", k)
    k = k + 1
    
f = 4

while (f < 5):
    print ("F ke ", f)
    f = f + 1
    
# Switch Case Python

era = 4

match (era):
    
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
        
    case _:
        print ("Biasa")
    
# Function Python
    
def iron ():
    print ("Hello Rusi")
    
iron ()
iron ()
iron ()

def teks (teks):
    print ("Hallo " + teks)
    
teks ("Junker")
teks ("Ragak")
teks ("Ebu Gaga")


def kurang (a, y):
    return a - y
    
hasil = kurang (10, 2)
print (hasil)

def kali (e, r):
    return e * r
    
hasil = kali (2,5)
print (hasil)

def pangkat (t, y):
    return t ** y
    
hasil = pangkat (2, 3)
print (hasil)

def kurang (c, b):
    return c - b
    
hasil = kurang (10, 4)
print (hasil)