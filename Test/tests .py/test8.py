import qrcode

vcard = '''BEGIN:VCARD
VERSION:4.0
FN:%s
TEL;TYPE=cell:%s
TEL;TYPE=home:%s
EMAIL:%s
ADR;TYPE=home:;;Rua xxx;Marinha Grande;Leiria;2400-231;Portugal
ORG:Bubba Gump Shrimp Co.
ADR;TYPE=WORK:;;Rua xxx;Marinha Grande;Leiria;;Portugal
TITLE:Shrimp Man
END:VCARD'''

vcard = vcard % ("Antonio", "968756886", "156982656", "ajshduasfg@haspos.com")


qr = qrcode.QRCode(
    version=4,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=5,
    border=4,
)
qr.add_data(vcard)
qr.make(fit=True)
img = qr.make_image()
img.save('1.jpg')
