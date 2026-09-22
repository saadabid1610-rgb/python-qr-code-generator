import qrcode

data = input("Enter your text or URL: ").strip()

filename = input("Enter your file name: ").strip()

if not filename.endswith(".png"):
    filename += ".png"

qr = qrcode.QRCode(box_size=10, border=4)

qr.add_data(data)

img = qr.make_image(fill_color="black", back_color="white")

img.save(filename)

print(f"QR code saved as {filename}")