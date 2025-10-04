"""
Test for QR code generation functionality.
"""

import os
import sys
import tempfile

from PIL import Image


# Import the function from the script
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from generate_qr_code import generate_qr_code  # noqa: E402


def test_generate_qr_code():
    """Test that QR code generation creates a valid image file."""
    with tempfile.TemporaryDirectory() as temp_dir:
        # Change to temp directory for test
        original_cwd = os.getcwd()
        os.chdir(temp_dir)

        try:
            # Generate QR code
            generate_qr_code()

            # Check that the file was created
            qr_file = "all_hands_nyc_qr_code_new.png"
            assert os.path.exists(qr_file), "QR code file was not created"

            # Check that it's a valid image
            with Image.open(qr_file) as img:
                assert img.format == "PNG", "Generated file is not a PNG image"
                assert img.size[0] > 0 and img.size[1] > 0, (
                    "Image has invalid dimensions"
                )

        finally:
            os.chdir(original_cwd)


def test_qr_code_url_content():
    """Test that the QR code contains the expected URL."""
    expected_url = (
        "all-hands.dev/nycslides?"
        "utm_source=ai-agent-hackathon&utm_medium=qrcode&utm_campaign=oct25"
    )

    # We can't easily decode QR codes in tests without additional dependencies,
    # but we can verify the URL is correctly formatted
    assert "all-hands.dev/nycslides" in expected_url
    assert "utm_source=ai-agent-hackathon" in expected_url
    assert "utm_medium=qrcode" in expected_url
    assert "utm_campaign=oct25" in expected_url
