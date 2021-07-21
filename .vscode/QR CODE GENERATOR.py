import qrcode
import image
qr = qrcode.QRCode(
    version = 15, # more version increases the size of the image and more complicated picture.
    box_size = 10, # size of the box.
    border = 5 # border in all 4 sides with white color.
)
print("Please copy paste the url of any website to generate the QRCODE of that website.")
data = input()
# this entire path will be converted into a QR CODE. So that any one can access the information  with one scan with there mobile device.
qr.add_data(data)
qr.make(fit = True)
img = qr.make_image(fill="black",black_color = "white")
img.save("test.png")