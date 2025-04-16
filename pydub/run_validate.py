"""
run_validate.py
run functions defined in validate.py
"""
from validate import generate_comparison_files, validate_files

if __name__ == '__main__':
    generate_comparison_files()
    validate_files()
