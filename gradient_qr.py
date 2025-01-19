import time
import qrcode
from PIL import Image, ImageDraw


# Data for the QR code
data = input("Enter link to be encoded in QR:")


def create_gradient_qr(data, gradient_colors, output_file):
    # Create a QR Code object
    qr = qrcode.QRCode(
        version=1,  # Controls the size of the QR code (1 is the smallest, up to 40)
        error_correction=qrcode.constants.ERROR_CORRECT_H,  # High error correction
        box_size=10,  # Size of each box in the QR code
        border=4,  # Border size (minimum is 4)
    )

    # Add data to the QR code
    qr.add_data(data)
    qr.make(fit=True)

    # Generate the QR code as an image
    qr_img = qr.make_image(fill_color="black", back_color="white").convert("RGB")
    width, height = qr_img.size

    # Create a new image for the gradient effect
    gradient_qr = Image.new("RGB", qr_img.size, "white")
    draw = ImageDraw.Draw(gradient_qr)

    # Define the gradient colors
    r1, g1, b1 = gradient_colors[0]  # Start color (pink)
    r2, g2, b2 = gradient_colors[1]  # Middle color (blue)
    r3, g3, b3 = gradient_colors[2]  # End color (green)

    # Apply gradient to the QR code blocks
    for y in range(height):
        for x in range(width):
            if qr_img.getpixel((x, y)) == (0, 0, 0):  # Black block
                # Calculate gradient color based on position
                ratio = y / height  # Vertical gradient
                if ratio < 0.5:  # Pink to Blue
                    r = int(r1 + (r2 - r1) * (ratio * 2))
                    g = int(g1 + (g2 - g1) * (ratio * 2))
                    b = int(b1 + (b2 - b1) * (ratio * 2))
                else:  # Blue to Green
                    r = int(r2 + (r3 - r2) * ((ratio - 0.5) * 2))
                    g = int(g2 + (g3 - g2) * ((ratio - 0.5) * 2))
                    b = int(b2 + (b3 - b2) * ((ratio - 0.5) * 2))

                draw.point((x, y), fill=(r, g, b))

    # Save the gradient QR code
    gradient_qr.save(output_file)
    print(f"Gradient QR code saved as {output_file}")



gradient_colors = [(255, 105, 180), (30, 144, 255), (50, 205, 50)]  # Pink, Blue, Green
file_name = str(time.time())
output_file = f"{file_name}.png"

# Create the gradient QR code
create_gradient_qr(data, gradient_colors, output_file)
