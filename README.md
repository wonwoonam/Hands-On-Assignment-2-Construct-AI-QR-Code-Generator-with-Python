# QR Code Generator for Biox Systems

## 📌 Assignment Task

Construct a **QR code generator** at **Biox Systems** using Python.

This project generates a scannable QR code pointing to Biox Systems' official website and displays it in a simple popup window.

---

## ✅ Output

The final output is a GUI window that displays a QR code with the following layout:

- **QR Code Content:**  
  `https://www.bioxsystems.com`

- **Display:**  
  A popup window showing the QR code image

- **Generated Image:**  
  A `biox_qr.png` file is also saved in the current directory.

---

## 🛠️ Technologies Used

- Python 3.7+
- [`qrcode`](https://pypi.org/project/qrcode/)
- [`Pillow`](https://pypi.org/project/Pillow/)
- Built-in `tkinter` module for GUI display

---

## 🚀 How to Run

1. **Clone or Download** 
    Clone this project.

2. **Install dependencies**:
    pip install qrcode[pil] pillow

2. **Run**:
    python qr_popup.py