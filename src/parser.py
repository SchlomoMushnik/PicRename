import os
import pandas as pd
from exif import get_DateTimeOriginal


def scan_pics_recursive(path):
    """
    Recursively scan all folders down to the bottom and return a list of all file paths.
    
    Args:
        path: Root directory path to start scanning from
        
    Returns:
        List of absolute paths to all files found recursively
    """
    the_list = []
    for root, dirs, files in os.walk(path):
        for file in files:
            filepath = os.path.join(root, file)          
            the_list.append(os.path.abspath(filepath))
    return the_list


def scan_pics(path):
    """
    List all files in a directory and return as pandas DataFrame.
    
    Args:
        path: Directory path to list files from
        
    Returns:
        DataFrame with columns: index, filename, extension, absolute_path,
    """

    new_filename = ""          # leerer String-Instanz
    DateTimeOriginal = ""      # leerer String (falls erwartet)

    the_list = scan_pics_recursive(path)
    
    data = []
    for idx, filepath in enumerate(the_list, 1):
        filename = os.path.basename(filepath)
        # Skip directories
        if not os.path.isfile(filepath):
            continue
            
        # Get file extension
        _, extension = os.path.splitext(filename)
        
        # Get absolute path
        abs_path = os.path.abspath(filepath)

        
        
        data.append({
            'Index': idx,
            'Source Year': source_year,
            'Source Month': source_month,
            'Source Filename': source_filepath,
            'Extension': extension,
            'Converted': converted,
            'DateTimeOriginal': DateTimeOriginal,
            'Target Year': target_year,
            'Target Month': target_month,
            'New Filename': new_filename
        })
    
    df = pd.DataFrame(data)
    return df