

def test_get_jpg_DateTimeOriginal():
    from src.exif import get_jpg_DateTimeOriginal  # Ensure this function is defined in src.exif
    from datetime import datetime

    pfad = "test/data/01d1a908976ec820cc8e89847151280bb37df94bbe_00001.jpg"
    dt = get_jpg_DateTimeOriginal(pfad)
    assert dt == datetime(2020, 1, 20, 18, 31, 58)
    
def test_convert_png_to_jpg():
    from src.exif import convert_png_to_jpg  # Ensure this function is defined in src.exif
    from pathlib import Path
    import os

    pfad = "test/data/IMG_6277.PNG"
    jpg_path = convert_png_to_jpg(pfad)
    assert jpg_path is not None
    assert Path(jpg_path).exists()
    
    # Clean up created JPG file after test
    os.remove(jpg_path)