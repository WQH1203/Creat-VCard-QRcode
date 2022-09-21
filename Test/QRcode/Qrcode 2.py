import qrcode

qr = qrcode.QRCode(
    version=5,
    error_correction=qrcode.constants.ERROR_CORRECT_M,
    box_size=5,
    border=1,
)
f = open('data.txt', encoding="utf-8")

data_1 = f.read()

qr.add_data(data_1)

qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")

img.save('qrcode2.png')

img.show()

f.close()
