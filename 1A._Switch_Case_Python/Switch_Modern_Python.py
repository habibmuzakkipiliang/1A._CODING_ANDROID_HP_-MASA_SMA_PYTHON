r = 4

match (r):
    
    case 1:
        nama_yui = "Senin"
    case 2:
        nama_yui = "Selasa"
    case 3:
        nama_yui = "Rabu"
    case 4:
        nama_yui = "Kamis"
    case 5:
        nama_yui = "Jumat"
    case _:
        nama_yui = "Hari default"

print (nama_yui)


t = 6

match (t):
    
    case 1:
        angka_mar = "Senin"
    case 2:
        angka_mar = "Selasa"
    case 3:
        angka_mar = "Rabu"
    case 4:
        angka_mar = "Kamis"
    case 5:
        angka_mar = "Jumat"
    case _:
        angka_mar = "Hari biasa"
        
print (angka_mar)
