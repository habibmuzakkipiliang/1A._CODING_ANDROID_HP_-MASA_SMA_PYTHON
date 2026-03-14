# percabangan dasar

t = 8

if t > 5:
    print ("Besar")
else:
    print ("kecil")
    

# percabangan lanjutan 1

k = 10

if k < 5:
    print ("besar")
    
elif k > 5:
    print ("kecil")
else:
    print ("sama saja")
    
    
# percabangan lanjutan 2


m = 10

if m > 5:
    print ("Besar")
elif m < 5:
    print ("kecil")
else:
    print ("sama saja")
    
    
# percabangan nested 1

n = 10

if n > 5:
    if (True):
        print ("Besar")
    elif n < 5:
        print ("Kecil")
    elif n == 4:
        print ("4")
    elif n == 3:
        print ("3")
else:
    print ("semula")
    
# percabangan nested 2

w = 10

if w > 5:
    if (True):
        print ("Besar")
    elif w > 5:
        print ("kecil")
    elif w == 7:
        print ("7")
    elif w == 6:
        print ("6")
    elif w == 5:
        print ("5")
else:
    print ("semula")
    
# perulangan for

for i in range (1, 6):
    print ("i", i)
    
for k in range (6, 11):
    print ("k", k)
    
for d in range (6, 11):
    if d == 8:
        continue
    print ("D", d)
    
for g in range (10, 16):
    if g == 5:
        break
    print ("G", g)
    
for jk  in range (16, 21):
    if jk == 10:
        continue
    print ("jk", jk)

# perulangan while

e = 0

while (e < 6):
    print ("e", e)
    e = e + 1
    
r = 0

while (r < 5):
    print ("r", r)
    r = r + 1
    
    
q = 0

while (q < 10):
    print ("q", q)
    q = q + 1
    
h = 0

while (h < 6):
    print ("h", h)
    h = h + 1
    
s = 0

while (s < 5):
    print ("s", s)
    s = s + 1
    
    
# switch case


nilai = 6

match (nilai):
    case 1:
        print ("1")
        
    case 2:
        print ("2")
        
    case 3:
        print ("3")
        
    case 4:
        print ("4")
        
    case 5:
        print ("5")
        
    case 6:
        print ("6")
        
    case 7:
        print ("7")
        
    case 8:
        print ("8")
        
    case 9:
        print ("9")
        
    case 10:
        print ("10")
        
    case _:
        print ("semula")