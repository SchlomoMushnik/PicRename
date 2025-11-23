from pathlib import Path
from typing import Optional, Union
from datetime import datetime
from PIL import Image, ExifTags

def get_jpg_DateTimeOriginal(pfad: Union[str, Path]) -> Optional[datetime]:
    """
    Liest das EXIF-Feld 'DateTimeOriginal' aus der Bilddatei unter 'pfad'.
    Rückgabe: datetime-Objekt bei Erfolg, sonst None.
    """
    p = Path(pfad)
    if not p.exists():
        return None

    try:
        with Image.open(p) as img:
            exif = img._getexif()
    except Exception:
        return None

    if not exif:
        return None

    # Tag-ID für DateTimeOriginal ermitteln
    tag_id = None
    for k, v in ExifTags.TAGS.items():
        if v == "DateTimeOriginal":
            tag_id = k
            break

    if tag_id is None:
        return None

    val = exif.get(tag_id)
    if not val:
        return None

    if isinstance(val, bytes):
        try:
            val = val.decode("utf-8", errors="ignore")
        except Exception:
            val = val.decode(errors="ignore")

    # Erwartetes Format: "YYYY:MM:DD HH:MM:SS"
    try:
        return datetime.strptime(val, "%Y:%m:%d %H:%M:%S")
    except Exception:
        # Zusatzformate versuchen
        for fmt in ("%Y-%m-%d %H:%M:%S", "%Y:%m:%d", "%Y-%m-%d"):
            try:
                return datetime.strptime(val, fmt)
            except Exception:
                continue

    return None