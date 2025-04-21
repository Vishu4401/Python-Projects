# Import the qrcode library and alias it as qr
import qrcode as qr
# This allows us to access the classes and functions from the core part of the library (like QRCode)
import qrcode.main

# Changes the functionalities
# Creating instance of class QRCode
# version -> It controls the size of the QR Code (Version1 is 21*21 modules);
# error_correction -> Sets Error correction to High (H), which allows ~30% of the QR code to be damaged, but it can still be scanned;
# box_size -> Each box or pixels in QR code will be 10*10 Pixels
# border -> Thickness of the border, minimum is 4
qr_code_instance = qrcode.main.QRCode(version=1, error_correction=qr.constants.ERROR_CORRECT_H, box_size=10, border=4)

# Taking user based input for the link
web_link = input("Enter the URL to generate the QR Code: ")

# Adding the data to qrcode object
qr_code_instance.add_data(web_link)

# Automatically adjusts the QR code size to fit the data if needed
qr_code_instance.make(fit=True)

# Converts the QR Matrix into an image, based on the color specified
image = qr_code_instance.make_image(fill_color = "black", back_color = "white")
# Saving the image based on the name
image.save("website.png")
print("QR Code generated successfully!")
