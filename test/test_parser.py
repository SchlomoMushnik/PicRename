
import sys
from pathlib import Path

import pytest
from parser import scan_pics

# src zum Python-Pfad hinzufügen (eine Ebene hoch, dann src/)
sys.path.append(str(Path(__file__).resolve().parents[1] / "src"))

print("TEST IMPORT PATH:", Path(__file__).resolve().parents[1] / "src")
print("PYTHONPATH:", sys.path)

def test_scan_pics():
    path = "/Volumes/Acasis/iCloud 2020 Test/2020"
    df = scan_pics(path)
    print(df)
    assert not df.empty
    
    
    
