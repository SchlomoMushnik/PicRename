

def test_get_DateTimeOriginal():
    from src.exif import get_DateTimeOriginal
    from datetime import datetime

    pfad = "test/data/01d1a908976ec820cc8e89847151280bb37df94bbe_00001.jpg"
    dt = get_DateTimeOriginal(pfad)
    assert dt == datetime(2020, 1, 20, 18, 31, 58)