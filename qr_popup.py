import qrcode
from tkinter import Tk, Label
from PIL import Image, ImageTk

# Step 1: Generate QR Code
qr = qrcode.QRCode(box_size=10, border=4)
qr.add_data("https://www.bioxsystems.com")
qr.make(fit=True)

img = qr.make_image(fill="black", back_color="white")
img.save("biox_qr.png")  # optional: save image

# Step 2: Display it in a popup window using Tkinter
root = Tk()
root.title("Scan QR Code")
root.resizable(False, False)

# Convert PIL image to Tkinter-compatible image
tk_img = ImageTk.PhotoImage(img)

# Add to label and show
label = Label(root, image=tk_img)
label.pack()

# Keep window open
root.mainloop()
