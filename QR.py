import qrcode

URL=input("Enter the URL to generate QR code: ")
# Input data for the QR code
input_data = URL#"https://www.w3schools.com/"

# Create QR code instance
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=100,
    border=5,
)

# Add data to the QR code
qr.add_data(input_data)
qr.make(fit=True)

# Create an image from the QR Code instance
img = qr.make_image(fill_color="black", back_color="white")

# Save the image
img.save("my_qrcode.png")

print("QR code generated and saved as my_qrcode.png for data:", input_data)

#Display the QR image
img.show()