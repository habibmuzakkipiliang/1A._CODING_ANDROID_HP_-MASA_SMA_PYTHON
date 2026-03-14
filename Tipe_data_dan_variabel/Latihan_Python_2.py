print ("Hello World")

a = "Belajar Coding Python \n" .upper ()
b = "Halo Coding Python \n" .lower ()

hasil = a + b
print (hasil)

zoom = "Halo Anak MAN 2 Hebat"

print (zoom .upper())
print (zoom .lower())
print (zoom .capitalize())
print (zoom .swapcase())
print (zoom .replace("Hebat", "Keren \n"))

a = 50

if a > 23 :
    print ("Besar")
elif a < 23 :
    print ("Kecil")
else :
    print ("Sama saja")
    
print ("\n")
    
b = 1

for b in range (1, 9):
    print ("Perulangan ke -", b)
    
k = 9

for k in range (9, 15):
    if k == 10:
        continue
    print ("Perulangan ke- ", k)