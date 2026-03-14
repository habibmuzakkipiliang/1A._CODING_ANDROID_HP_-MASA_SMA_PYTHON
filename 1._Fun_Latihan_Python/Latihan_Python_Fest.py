# percabangan biasa

r = 4

if r > 3:
    print ("Besar")
elif r < 5:
    print ("Kecil")
else:
    print ("Sama saja")
    
# percabangan nested
    
x = 10
cek = True

if x > 9:
    if x == True:
        print ("Besar")
    elif x < 11:
        print ("Kecil")
else:
    print ("Sama saja")

# perulangan for

k = ["Felicia", "Cimi", "Degen", "Rurik"]

for item in k:
    print (item)
    
for item in k:
    print (k)
    
for item in sorted (k):
    print (item)
    
for i in range (0, 10):
    print ("Range ke - ", i)
    
# while

r = 0

while (r < 5):
    print ("while ke - ", r)
    r = r + 1