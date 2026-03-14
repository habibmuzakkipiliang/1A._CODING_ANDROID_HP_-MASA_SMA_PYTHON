# percabangan biasa

x = 4

if x > 5:
    print ("Besar")
elif x < 3:
    print ("Kecil")
else:
    print ("Sama saja")
    
y = 4
cek = True

if y > 4:
    if y == True:
        print ("Besar")
    elif y < 4:
        print ("Kecil")
else:
    print ("Sama saja")

# for python

for i in range (0, 5):
    print ("For", i)
    
ar = ["Ratar", "Nawal", "Best"]

for item in ar:
    print (item)
    
for item in ar:
    print (ar)
    
# while python

t = 0

while (t < 5):
    print ("while ", t)
    t = t + 1
    
m = 0

while (m < 5):
    print ("wain ", m)
    m = m + 1
    
# switch case

match (i):
    case 1:
        print ("Senin")
    case 2:
        print ("Selasa")
    case 3:
        print ("Rabu")
    case 4:
        print ("Kamis")
    case _:
        print ("Hari biasa")
        


f = 3

match (f):
    case 1:
        print ("Fagos")
    case 2:
        print ("Hugos")
    case 3:
        print ("Sabler")
    case 4:
        print ("Namro")
    case 5:
        print ("Hiro")
    case _:
        print ("Default")