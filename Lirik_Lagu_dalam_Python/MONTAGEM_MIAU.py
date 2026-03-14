import time
import sys

def cetak_berwarna(teks, warna_kode):
    """Fungsi untuk mencetak teks dengan warna ANSI."""
    # Kode warna: Cyan = 96, Kuning = 93, Hijau = 92, Merah = 91
    return f"\033[{warna_kode}m{teks}\033[0m"

def lirik_animasi(teks, delay_karakter=0.05):
    """Memberikan efek mengetik (typing effect) per karakter."""
    for karakter in teks:
        sys.stdout.write(karakter)
        sys.stdout.flush()
        time.sleep(delay_karakter)
    print() # Pindah baris setelah lirik selesai

def jalankan_karaoke(daftar_lirik):
    """Menjalankan urutan lirik dengan durasi tertentu."""
    print("\n" + "="*40)
    print(cetak_berwarna("   NOW PLAYING: MONTAGEM MIAU (Slowed)   ", 93))
    print("="*40 + "\n")
    
    time.sleep(1) # Jeda awal sebelum mulai

    for bait in daftar_lirik:
        kalimat = bait["teks"]
        warna = bait.get("warna", 96) # Default Cyan
        delay_ketik = bait.get("kecepatan", 0.06)
        jeda_setelah = bait.get("jeda", 0.5)

        # Cetak lirik dengan animasi
        sys.stdout.write(f"\033[{warna}m") # Mulai warna
        lirik_animasi(kalimat, delay_ketik)
        
        # Jeda antar baris lirik
        time.sleep(jeda_setelah)

# --- KONFIGURASI LIRIK ---
# Format: teks lirik, kode warna, kecepatan ketik, dan jeda ke baris berikutnya
lirik_lagu = [
    {"teks": "Pobre mi gatito...", "warna": 96, "kecepatan": 0.1, "jeda": 0.5},
    {"teks": "Alguien le ha pegado...", "warna": 96, "kecepatan": 0.08, "jeda": 0.5},
    {"teks": "Por comer un loncito...", "warna": 96, "kecepatan": 0.08, "jeda": 0.5},
    {"teks": "Ahora está llorando.", "warna": 91, "kecepatan": 0.12, "jeda": 1.2},
    
    {"teks": "\n(Chorus)", "warna": 93, "kecepatan": 0.01, "jeda": 0.5},
    {"teks": "¡Ay mi gatito! ¡Miau, miau, miau!", "warna": 92, "kecepatan": 0.05, "jeda": 0.4},
    {"teks": "¡Ay mi gatito! ¡Miau, miau, miau!", "warna": 92, "kecepatan": 0.05, "jeda": 0.4},
    {"teks": "¡Ay mi gatito! ¡Miau, miau, miau!", "warna": 92, "kecepatan": 0.05, "jeda": 0.4},
    {"teks": "¡Ay mi gatito! ¡Miau, miau, miau!", "warna": 92, "kecepatan": 0.05, "jeda": 1.5},

    {"teks": "\nSe comió la carne, se comió el pescado...", "warna": 96, "kecepatan": 0.07, "jeda": 0.6},
    {"teks": "Se comió todito, nada me ha dejado.", "warna": 96, "kecepatan": 0.07, "jeda": 1.0},
    
    {"teks": "\n[Fin de la canción]", "warna": 93, "kecepatan": 0.05, "jeda": 0}
]

if __name__ == "__main__":
    try:
        jalankan_karaoke(lirik_lagu)
    except KeyboardInterrupt:
        print("\n\n" + cetak_berwarna("Program dihentikan.", 91))
        