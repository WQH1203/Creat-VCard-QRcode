import qrcode

img = qrcode.make('https://www.vidrala.com/en/contact/santos-barosa/')

with open('qrcode.png', 'wb') as f:
    img.save(f)
