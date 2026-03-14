import time
import sys

# Definisi Warna menggunakan ANSI Escape Codes
CYAN = "\033[96m"
YELLOW = "\033[93m"
GREEN = "\033[92m"
BOLD = "\033[1m"
RESET = "\033[0m"

def typing_effect(text, delay=0.05):
    """
    Memberikan efek animasi pengetikan per karakter.
    """
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print() # Pindah baris setelah selesai

def play_karaoke(lyrics_data):
    """
    Menjalankan simulasi lirik karaoke.
    lyrics_data berisi tuple: (teks_lirik, jeda_sebelum_baris_berikutnya, kecepatan_ketik)
    """
    print(f"{YELLOW}{BOLD}=== JKT48 - FLYING HIGH (KARAOKE MODE) ==={RESET}\n")
    time.sleep(1)

    for line, pause, type_speed in lyrics_data:
        # Menampilkan lirik dengan warna Cyan
        sys.stdout.write(CYAN)
        typing_effect(line, type_speed)
        sys.stdout.write(RESET)
        
        # Jeda antar baris lirik
        time.sleep(pause)

# Data Lirik: (Teks, Jeda Antar Baris, Kecepatan Ketik)
# Catatan: Nilai ini bisa kamu sesuaikan dengan tempo lagu aslinya
flying_high_lyrics = [
    ("I'm sittin' pretty and enjoyin' the view", 0.5, 0.04),
    ("We're flyin' higher, higher", 1.0, 0.06),
    ("Feels like this gon' call for celebration", 0.5, 0.04),
    ("I made it from the bottom to the top", 0.8, 0.04),
    ("Finally feeling emancipated", 0.5, 0.05),
    ("I can hardly believe I made it this far", 1.2, 0.04),
    ("---", 0.5, 0.1), # Transisi
    ("I feel the wave, I feel the love", 0.3, 0.03),
    ("I feel the energy", 0.5, 0.03),
    ("I'm on my way to better days", 0.3, 0.03),
    ("There ain't nothing that can stop me now!", 1.0, 0.05),
    ("\n", 0.1, 0.01),
    (f"{GREEN}I'm sittin' pretty and enjoyin' the view{RESET}", 0.3, 0.04),
    (f"{GREEN}We're flyin' higher, higher!{RESET}", 2.0, 0.06),
]

if __name__ == "__main__":
    try:
        play_karaoke(flying_high_lyrics)
        print(f"\n{YELLOW}Terima kasih telah bernyanyi!{RESET}")
    except KeyboardInterrupt:
        print(f"\n{YELLOW}Karaoke dihentikan.{RESET}")
        