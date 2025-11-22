import os
import pandas as pd


def scan_pics(path):
    """
    List all files in a directory and return as pandas DataFrame.
    
    Args:
        path: Directory path to list files from
        
    Returns:
        DataFrame with columns: index, filename, extension, absolute_path
    """
    files = os.listdir(path)
    
    data = []
    for idx, filename in enumerate(files, 1):
        filepath = os.path.join(path, filename)
        
        # Skip directories
        if not os.path.isfile(filepath):
            continue
            
        # Get file extension
        _, extension = os.path.splitext(filename)
        
        # Get absolute path
        abs_path = os.path.abspath(filepath)
        
        data.append({
            'Index': idx,
            'Filename': filename,
            'Extension': extension,
            'Absolute_Path': abs_path
        })
    
    df = pd.DataFrame(data)
    return df