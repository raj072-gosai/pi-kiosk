import qrcode

# Define the URL to be embedded in the QR code
url = "http://192.168.144.26/menu.php?table_number=1"  # Replace with your desired webpage URL

# Generate the QR code
qr = qrcode.QRCode(
    version=1,  # Controls the size of the QR Code
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
    box_size=10,  # Size of each box in the QR Code grid
    border=4,  # Border size (minimum is 4)
)

# Add the URL to the QR code
qr.add_data(url)
qr.make(fit=True)

# Create the QR code image
img = qr.make_image(fill_color="black", back_color="white")

# Save the QR code image
img.save("table_1_qr_code.png")

print("QR code generated and saved as 'webpage_qr_code.png'.")

 
