
## 📦 QR Code Generator - Python

### 🧾 Description
This project is a simple command-line Python application that generates a QR Code from a URL input provided by the user. The QR code is created using the `qrcode` library and saved as a PNG image file. It's an excellent beginner-friendly example to understand how QR codes work and how they can be generated programmatically using Python.

---

### 🚀 Features
- Generates a QR Code for any URL or string input.
- Uses **high error correction**, allowing the QR code to be readable even if ~30% of it is damaged.
- Customizable size, color, and border settings.
- Saves the QR code as an image file locally.

---

### 🛠️ How It Works

1. **Library Imports**  
   The `qrcode` library is imported and aliased as `qr`. The core functionalities are accessed via `qrcode.main`.

2. **QR Code Configuration**  
   - **Version 1** is used, which generates a 21x21 matrix QR code. This version is suitable for short strings or links.
   - **High error correction level (H)** is set, allowing for up to 30% damage tolerance.
   - **Box Size** is set to 10 pixels, meaning each square in the QR code will be 10x10 pixels.
   - **Border** is set to 4, which is the minimum recommended border thickness.

3. **User Input**  
   The user is prompted to input a URL or any text data that should be encoded into the QR code.

4. **Data Encoding**  
   The input data is added to the QR code object using `add_data()`.

5. **Optimization and Image Generation**  
   - The `make(fit=True)` function optimizes the QR matrix size to fit the data.
   - The QR matrix is then rendered into an image with **black fill color** and **white background**.

6. **Image Saving**  
   The generated QR code image is saved as `website.png` in the current working directory.

7. **Success Message**  
   The script notifies the user once the QR code is successfully generated and saved.

---

### 📂 Output
- The QR code is saved as a file named **`website.png`**.
- It can be scanned using any QR scanner or phone camera to verify the encoded content.

---

### ✅ Requirements
- Python 3.x
- `qrcode` library  
  Install it using pip:
  ```bash
  pip install qrcode[pil]
  ```

---

### 📌 Use Cases
- Sharing WiFi credentials, contact details, or URLs.
- Embedding QR codes in digital or printed documents.
- Quick and easy way to redirect users to a website via scan.

---

### 📄 License
This project is open source and available under the [MIT License](LICENSE).
