import qrcode

print("=== QR CODE GENERATOR ===")

data= input("Enter text or URl:")
filename=input("Enter file name:")

qr=qrcode.make(data)
qr.save(filename + ".png")

print("QR code generated successfully!")
print("Saved as:",filename + ".png")