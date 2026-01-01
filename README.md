# Game-Flappy-Bird

Game **Flappy Bird versi Deluxe** yang dibuat menggunakan **Python & Pygame**, dengan tampilan menu awal yang menarik, audio, serta **sistem High Score yang tersimpan otomatis**.

---

## ✨ Fitur Utama
- 🎮 **Menu Awal Interaktif**
  - Judul dengan efek bayangan
  - Burung animasi floating di tengah
  - Teks *Press SPACE to Start* berkedip
- 🔊 **Audio**
  - Sound lompat
  - Sound skor
  - Sound game over
- 🏆 **High Score System**
  - Disimpan otomatis ke file
  - Tidak hilang saat game ditutup
  - Ditampilkan di Menu dan Game Over
- 🐦 Burung PNG transparan
- 📊 Sistem skor
- 💥 Deteksi tabrakan
- ⏱️ FPS stabil (60 FPS)

---

## 🧰 Teknologi
- Python 3.x
- Pygame

---

## 📁 Struktur Folder
```
FlappyBird/
│
├── flappy_bird.py
├── bird.png
├── README.md
├── jump.wav
├── score.wav
├── gameover.wav
├── highscore.txt # otomatis dibuat
└── README.md
```

> ⚠️ Pastikan file `bird.png`, `jump.wav`, `score.wav`, `gameover.wav` berada di **folder yang sama** dengan `flappy_bird.py`

---

## ▶️ Cara Menjalankan Game

### 1️⃣ Install Pygame
```bash
pip install pygame
```

### 2️⃣ Jalankan Program
```bash
python flappy_bird.py
```

---

## 🎮 Kontrol Game
| Tombol | Fungsi |
|------|-------|
| SPACE | Lompat/Start/Restart |
| ESC | Kembali ke Menu |
| Close Window | Keluar dari game |

---

## 🧠 Alur Game
```
MENU
 ↓ SPACE
PLAYING
 ↓ Tabrakan
GAME OVER
 ↓ SPACE → Restart
 ↓ ESC   → Menu
```

---


## 🚀 Pengembangan Selanjutnya
- 🎶 Background music (menu & gameplay)
- ⭐ Efek NEW HIGH SCORE
- 🖱️ Tombol menu menggunakan mouse
- 💾 Simpan nama pemain
- 📦 Export game menjadi file .exe

---
