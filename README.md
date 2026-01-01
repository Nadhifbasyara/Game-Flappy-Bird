# Game-Flappy-Bird

Game **Flappy Bird sederhana** yang dibuat menggunakan **Python** dan **Pygame**, dengan karakter burung menggunakan **gambar PNG transparan**.

---

## 🎮 Fitur Game
- Kontrol sederhana (tekan **SPACE** untuk terbang)
- Menggunakan gambar burung PNG (`convert_alpha`)
- Sistem skor
- Deteksi tabrakan dengan pipa
- Tampilan **Game Over** dan restart otomatis
- FPS stabil (60 FPS)

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
└── README.md
```

> ⚠️ Pastikan file `bird.png` berada di **folder yang sama** dengan `flappy_bird.py`

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
| SPACE | Terbang / Restart saat Game Over |
| Close Window | Keluar dari game |

---

## 🧠 Cara Kerja Singkat
- Burung bergerak ke bawah karena **gravitasi**
- Tekan **SPACE** untuk memberi gaya lompat
- Pipa bergerak dari kanan ke kiri
- Skor bertambah setiap pipa berhasil dilewati
- Game berakhir jika burung:
  - Menabrak pipa
  - Keluar dari layar

---


## 🚀 Pengembangan Selanjutnya
- Background scrolling
- Efek suara
- Animasi burung
- High score
- Menu awal

---
