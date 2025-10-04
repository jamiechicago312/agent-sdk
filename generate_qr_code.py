#!/usr/bin/env python3
"""
Script to generate QR code for All Hands NYC slides URL.
"""

import qrcode


def generate_qr_code():
    """Generate QR code for the All Hands NYC slides URL."""
    url = (
        "all-hands.dev/nycslides?"
        "utm_source=ai-agent-hackathon&utm_medium=qrcode&utm_campaign=oct25"
    )

    # Create QR code instance
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    # Add data to QR code
    qr.add_data(url)
    qr.make(fit=True)

    # Create QR code image
    img = qr.make_image(fill_color="black", back_color="white")

    # Save the QR code
    img.save("all_hands_nyc_qr_code_new.png")  # type: ignore[arg-type]
    print("QR code generated and saved as 'all_hands_nyc_qr_code_new.png'")
    print(f"URL encoded: {url}")


if __name__ == "__main__":
    generate_qr_code()
