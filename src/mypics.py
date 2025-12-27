import sys
from pathlib import Path
from work_dir import select_working_directory
from parser import scan_pics
from chart import show_chart
import shutil

sys.path.append(str(Path(__file__).resolve().parent))


def create_target_folder_structure(target_dir):
    target_path = Path(target_dir)
    for year in range(2000, 2027):  # 2027 is exclusive, so up to 2026
        year_path = target_path / str(year)
        year_path.mkdir(parents=True, exist_ok=True)
        for month in range(1, 13):
            month_str = f"{month:02d}"
            month_path = year_path / month_str
            month_path.mkdir(parents=True, exist_ok=True)

def main():
    
    debug = True
    if debug:
        working_dir = "/Volumes/Acasis/source_pics"
        target_dir = "/Volumes/Acasis/target_pics"
        target_path = Path(target_dir)
        source_path = Path(working_dir)
        
        if not target_path.exists():
            target_path.mkdir(parents=True)
            
    else:
        working_dir = select_working_directory()

    create_target_folder_structure(target_dir)
        
    df = scan_pics(working_dir)
    print(df)
    
    
    
    show_chart(df)
    
    


if __name__ == "__main__":
    main()
    
