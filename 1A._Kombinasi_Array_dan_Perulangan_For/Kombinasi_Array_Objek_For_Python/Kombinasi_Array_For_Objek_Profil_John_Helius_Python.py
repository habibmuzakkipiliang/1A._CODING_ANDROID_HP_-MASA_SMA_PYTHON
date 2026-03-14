data = {
    "nama" : "John Helius Rockerfound ",
    "kelas" : "Biligual Class",
    "lomba" : ["Informatic Olympiad", "Math Olypiad", "Physics Olympiad"],
    "sekolah" : "American Senior High School",
    "hobi" : ["Coding", "Baca Buku", "Travelling"],
    "coding" : ["HTML", "CSS", "JavaScipt", "Python"],
    "asal_negara" : "Amerika Serikat",
}

print ("Nama lengkap :", data ["nama"])

print ("Kelas :", data ["kelas"])

print ("Lomba :", data ["lomba"])

for s in data ["lomba"]:
    print (s)

print ("Sekolah :", data ["sekolah"])

print ("Hobi :", data ["hobi"])

for i in data ["hobi"]:
    print (i)
    
print ("Coding :", data ["coding"])

for u in data ["coding"]:
    print (u)
    
print ("Asal negara :", data ["asal_negara"])