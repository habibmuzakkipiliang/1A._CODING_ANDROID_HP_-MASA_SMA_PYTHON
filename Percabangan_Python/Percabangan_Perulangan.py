# Percabangan Biasa

r = 50

if r > 12:
    print ("Besar")
elif r < 13:
    print ("Kecil")
else:
    print ("Sama saja")
    
# Percabangan Nested

t = 55
cek = True

if t > 45:
    if (cek == True):
        print ("Besar")
    elif t < 45:
        print ("Kecil")
else:
    print ("Sama saja")

# Perulangan For

for i in range (0,3):
    print ("For ke -", i)
    
li = ["HP", "Acer", "Del", "Asus", "Macbook"]

for item in li:
    print (li)
    
for item in li:
    print (item)
    
for a in range (3,5):
    if a == True:
        continue
    print ("For = ", a)
    
for e in range (6,8):
    if e == False:
        break
    print ("For : ", e)
    
# perulangan while

j = 0

while (j < 5):
    print ("While ke - ", j)
    j = j + 3
    
k = 0
    
while (k < 10):
    print ("While i : ", k)
    k = k + 5
    
