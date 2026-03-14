nama = 3

match (nama):
    
    case 1:
        nama_sampel = "Senin"
    case 2:
        nama_sampel = "Selasa"
    case 3:
        nama_sampel = "Rabu"
    case 4:
        nama_sampel = "Kamis"
    case 5:
        nama_sampel = "Jumat"
    case _:
        nama_sampel = "Hari libur"
        
print (nama_sampel)