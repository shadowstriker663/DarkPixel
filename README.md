# 🔥 DarkPixel — Steganography Framework

DarkPixel is a hybrid steganography tool that securely hides files inside PNG images using:

* AES-256-GCM Encryption
* Adaptive LSB Steganography
* PNG Chunk Injection (Covert Container Mode)
* File Integrity Verification (SHA-256)

---

## ⚙️ Features

* Hide multiple files inside a PNG image
* Strong password-based encryption (PBKDF2 + AES-GCM)
* Automatic compression
* Stealth mode (secure file deletion)
* Dual-layer hiding:

  * LSB (covert)
  * PNG chunk (fallback container)

---

## 📦 Installation

```bash
git clone https://github.com/shadowstriker663/DarkPixel
cd darkpixel
pip install -r requirements.txt
```

---

## 🚀 Usage

```bash
python darkpixel.py
```

Follow the interactive menu.

---

## ⚠️ Disclaimer

This tool is for educational and ethical security research purposes only. Do not use for illegal activities.

---

## 👨‍💻 Author

ShadowStriker