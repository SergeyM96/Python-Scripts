import qrcode

# Input the URL
link = input("Paste Your URL Here: ")

# Generate the QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(link)
qr.make(fit=True)

# Create a PNG image
qr_img = qr.make_image()

# Ask the user to provide the name for the QR code image file
name_img = input("Name of image file (without extension): ")

# Save the QR code image in the same directory as the script
qr_img.save(f"{name_img}.png")

# Print a confirmation message
print(f"QR code saved as {name_img}.png in the same directory as the script.")
