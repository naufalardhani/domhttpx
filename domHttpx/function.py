import glob
import os
from pathlib import Path

from domHttpx import write

def check_result():
    result_dir = Path('./result')
    result_files = list(result_dir.glob('*'))
    
    for idx, file_path in enumerate(result_files, 1):
        print(f'{idx}. {file_path.name}')

def show_result(filename):
    result_path = Path('./result') / filename
    try:
        with open(result_path) as f:
            print(f.read())
    except FileNotFoundError:
        write.error(f"File {filename} not found.")
    except Exception as e:
        write.error(f"An error occurred while reading file: {str(e)}.")

def remove_result(filename):
    result_path = Path('./result') / filename
    
    with open(result_path) as f:
        line_count = sum(1 for _ in f)
    
    write.tab()
    confirm = input(f'Are you sure to remove {filename} which has {line_count} results? (y/n) ')
    
    if confirm.lower() == 'y':
        result_path.unlink()