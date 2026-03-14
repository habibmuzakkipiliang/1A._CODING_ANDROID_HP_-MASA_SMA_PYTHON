# luas dan keliling persegi

a = int (input ("Masukkan sisi persegi a :"))
b = int (input ("Masukkan sisi persegi b :"))

luas = a * b
keliling = 2 * (a + b)

print ("Luas persegi adalah :", luas)
print ("Keliling persegi adalah :", keliling)




# luas dan keliling segitiga

a = int (input ("Masukkan alas segitiga a :"))
t = int (input ("Masukkan tinggi segitiga t :"))
s = int (input ("Masukkan sisi miring segitiga s :"))

luas =  a * t / 2
keliling = a + t + s

print ("Luas segitiga adalah :", luas)
print ("Keliling segitiga adalah :", keliling)




# luas dan keliling lingkaran

r = int (input ("Masukkan jari-jari lingkaran r :"))
phi = 3.14
luas = phi * r * r
keliling = 2 * phi * r

print ("Luas lingkaran adalah :", luas)
print ("Keliling lingkaran adalah :", keliling)




# luas dan keliling jajaran genjang

a = int (input ("Masukkan alas jajaran genjang a :"))
t = int (input ("Masukkan tinggi jajaran genjang t :"))
s = int (input ("Masukkan sisi miring jajaran genjang s :"))

luas = a * t
keliling = 2 * (a + s)

print ("Luas jajaran genjang adalah :", luas)
print ("Keliling jajaran genjang adalah :", keliling)