import pytest
import tempfile
from pathlib import Path
import sys
import os
import shutil

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from mypics import create_target_folder_structure


def test_create_target_folder_structure():
    # Set the target directory
    target_dir = Path("/Volumes/Acasis/target_pics")
    create_target_folder_structure(str(target_dir))

    # Check that years 2000 to 2026 exist
    for year in range(2000, 2027):
        year_path = target_dir / str(year)
        assert year_path.exists(), f"Year {year} folder should exist"
        assert year_path.is_dir(), f"Year {year} should be a directory"

        # Check that months 01 to 12 exist inside each year
        for month in range(1, 13):
            month_str = f"{month:02d}"
            month_path = year_path / month_str
            assert month_path.exists(), f"Month {month_str} in {year} should exist"
            assert month_path.is_dir(), f"Month {month_str} in {year} should be a directory"

    # Check that no extra years are created
    years_in_dir = [d.name for d in target_dir.iterdir() if d.is_dir()]
    expected_years = [str(y) for y in range(2000, 2027)]
    assert set(years_in_dir) == set(expected_years), "Only years 2000-2026 should be created"
    
    # Remove all folders recursively under target_dir
    for item in target_dir.iterdir():
        if item.is_dir():
            shutil.rmtree(item)
    

