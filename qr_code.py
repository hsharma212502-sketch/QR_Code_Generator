import qrcode
from PIL import Image

# User input
data = input("Enter the link or text for the QR code: ")
box_size = int(input("Enter the box size (e.g., 10): "))
fg_color = input("Enter the foreground color (e.g., black, blue, red): ")
bg_color = input("Enter the background color (e.g., white, yellow): ")

qr = qrcode.QRCode(
    version=1,
    box_size=box_size,
    border=4
)
qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill_color=fg_color, back_color=bg_color)

img.show()
img.save("custom_qr.png")
