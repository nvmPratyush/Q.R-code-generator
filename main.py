import qrcode

def generate_qr_code(data, filename="qrcode.png"):
    # Create QR code instance
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    # Add data to the QR code
    qr.add_data(data)
    qr.make(fit=True)

    # Create an image from the QR code
    img = qr.make_image(fill_color="black", back_color="white")

    # Save the image to a file
    img.save(filename)

if __name__ == "__main__":
    # Example usage
    data_to_encode = "https://www.example.com"
    output_filename = "example-qr_code.png"
    generate_qr_code(data_to_encode, output_filename)
    print(f"QR Code generated and saved as {output_filename}")
