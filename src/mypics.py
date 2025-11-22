import sys
from pathlib import Path
from work_dir import select_working_directory
from parser import scan_pics

sys.path.append(str(Path(__file__).resolve().parent))


def main():
    working_dir = select_working_directory()
    if working_dir:
        print(f"Working Directory: {working_dir}")
    else:
        print("Abgebrochen")
        
    df = scan_pics(working_dir)
    print(df)

if __name__ == "__main__":
    main()