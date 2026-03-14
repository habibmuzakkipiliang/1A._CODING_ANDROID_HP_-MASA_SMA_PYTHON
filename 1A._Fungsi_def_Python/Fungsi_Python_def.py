# contoh dasar

def exam ():
    print ("Selamat datang di Exam aku")

exam ()
exam ()
exam ()

# contoh 1

def sapa_aku (sapa_aku):
    print (sapa_aku, "kamu sangat pandai")
    
sapa_aku ("Elizabeth")
sapa_aku ("Blanca")
sapa_aku ("Fang")

def smurf (smurf):
    print ("Halo", smurf)
    
smurf ("Brainy")


# contoh 2 return def

def kali (a, b):
    return a * b
    
hasil = kali (2, 5)
print ("Kali", hasil)

def pangkat (u, j):
    return u ** j 
    
hasil = pangkat (3, 3)
print (hasil)

def modulus (k, b):
    return k % b
    
hasil = modulus (2, 34)
print (hasil)