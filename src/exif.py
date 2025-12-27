from pathlib import Path
from typing import Optional, Union, Tuple
from datetime import datetime
from PIL import Image, ExifTags
import re


def get_DateTimeOriginal(pfad: Union[str, Path]) -> Tuple[Optional[datetime], bool]:
    """
    Liest das 'DateTimeOriginal' Datum aus einer Bilddatei (JPG oder PNG) unter 'pfad'.
    Rückgabe: datetime-Objekt bei Erfolg, sonst None.
    """
    p = Path(pfad)
    if not p.exists():
        return None, False

    suffix = p.suffix.lower()
    if suffix in (".jpg", ".jpeg", ".tiff", ".jfif"):
        return (get_jpg_DateTimeOriginal(p), False)
    elif suffix == ".png":
        jpg_path = convert_png_to_jpg(p)
        if jpg_path:
            return (get_jpg_DateTimeOriginal(jpg_path), True)
        else:
            return (None, False)
    else:
        return (None, False)


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

def convert_png_to_jpg(pfad: Union[str, Path]) -> Optional[Path]:
        """
        Konvertiert eine PNG-Bilddatei in das JPG-Format und speichert sie unter dem gleichen Namen mit der Endung .jpg.
        Rückgabe: Pfad zur neuen JPG-Datei bei Erfolg, sonst None.
        """
        p = Path(pfad)
        if not p.exists() or p.suffix.lower() != ".png":
            return None

        try:
            with Image.open(p) as img:
                rgb_img = img.convert("RGB")  # PNG kann Transparenz haben, daher Konvertierung zu RGB
                jpg_path = p.with_suffix(".jpg")
                rgb_img.save(jpg_path, "JPEG")
                return jpg_path
        except Exception:
            return None

