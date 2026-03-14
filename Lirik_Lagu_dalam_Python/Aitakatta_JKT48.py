import time
import sys

def print_kreatif(teks, warna="putih", delay=0.05):
    """
    Fungsi untuk mencetak teks dengan efek mengetik (typing effect)
    dan warna menggunakan ANSI Escape Codes.
    """
    # Kode ANSI untuk warna terminal
    colors = {
        "cyan": "\033[96m",
        "kuning": "\033[93m",
        "hijau": "\033[92m",
        "merah": "\033[91m",
        "putih": "\033[0m",
        "bold": "\033[1m"
    }
    
    warna_kode = colors.get(warna.lower(), colors["putih"])
    sys.stdout.write(warna_kode)
    
    # Animasi per karakter
    for char in teks:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    
    sys.stdout.write(colors["putih"] + "\n")

def jalankan_karaoke():
    # Header Program
    print("\033[2J\033[H") # Membersihkan layar terminal
    print_kreatif("=== JKT48 - AITAKATTA (INGIN BERTEMU) ===", "kuning", 0.1)
    print_kreatif("Status: Auto-scroll Mode Aktif\n", "hijau", 0.05)
    time.sleep(1)

    # List Lirik: (Teks, Delay per karakter, Jeda setelah baris selesai)
    lirik = [
        ("Aitakatta!", 0.08, 0.2),
        ("Aitakatta!", 0.08, 0.2),
        ("Aitakatta!", 0.08, 0.5),
        ("YES!", 0.1, 0.5),
        ("Aitakatta!", 0.08, 0.2),
        ("Aitakatta!", 0.08, 0.2),
        ("Aitakatta!", 0.08, 0.5),
        ("YES!", 0.1, 0.5),
        ("Denganmu...", 0.12, 1.5),
        
        ("\n--- [Verse] ---", "putih", 0.1),
        ("Bersepeda ku menanjak bukit itu", 0.07, 0.5),
        ("Mungkin itu peluh tenagaku kucucurkan darinya", 0.07, 0.8),
        ("Angin pun mulai mengembus", 0.07, 0.5),
        ("Kemejaku terasa masih kurang cepat", 0.07, 1.2),
        
        ("\n--- [Pre-Chorus] ---", "putih", 0.1),
        ("Akhirnya kusadari...", 0.09, 0.5),
        ("Perasaan sebenarnya...", 0.09, 0.8),
        ("Ini jalani sejujurnya", 0.07, 0.5),
        ("Hanya di jalanmu ku akan terus berlari", 0.06, 1.5),
        
        ("\n--- [Chorus] ---", "putih", 0.1),
        ("Jika kusuka, kan kukatakan suka", 0.06, 0.4),
        ("Tak kututupi, kukatakan sejujurnya", 0.06, 0.4),
        ("Jika kusuka, kan kukatakan suka", 0.06, 0.4),
        ("Dari hatiku terbuka kukatakan", 0.06, 1.0),
    ]

    for baris, *info in lirik:
        # Menentukan kecepatan ketik dan jeda
        kecepatan = info[0] if isinstance(info[0], float) else 0.05
        jeda_baris = info[1] if len(info) > 1 else 0.5
        
        # Memberikan warna Cyan untuk lirik utama
        warna = "cyan" if "---" not in baris else "kuning"
        
        print_kreatif(baris, warna, kecepatan)
        time.sleep(jeda_baris)

    print("\n")
    print_kreatif("Selesai. Terima kasih telah mendengarkan!", "hijau", 0.05)

if __name__ == "__main__":
    try:
        jalankan_karaoke()
    except KeyboardInterrupt:
        print("\n\nProgram dihentikan oleh pengguna.")
        sys.exit()
        