import os
import shutil
import pytest

from sort_files import main

# Define the test directory path
TEST_DIR = 'test_directory'

# Define the test files
TEST_FILES = ['test.txt', 'test.pdf', 'test.docx', 'test.xlsx', 'test.jpg', 'test.png', 'test.mp3', 'test.mp4']

# Define the expected directories and files
EXPECTED_DIRS = ['TextFiles', 'PDFs', 'WordDocs', 'ExcelDocs', 'Images', 'Music', 'Videos']
EXPECTED_FILES = {
    'TextFiles': ['test.txt'],
    'PDFs': ['test.pdf'],
    'WordDocs': ['test.docx'],
    'ExcelDocs': ['test.xlsx'],
    'Images': ['test.jpg', 'test.png'],
    'Music': ['test.mp3'],
    'Videos': ['test.mp4']
}

def setup_module():
    # Create the test directory and add the test files
    os.mkdir(TEST_DIR)
    for filename in TEST_FILES:
        with open(os.path.join(TEST_DIR, filename), 'w') as f:
            f.write('This is a test file')

def test_sort_files():
    # Run the sort_files function on the test directory
    main(TEST_DIR)
    
    # Check that the expected directories and files were created
    for directory in EXPECTED_DIRS:
        assert os.path.exists(os.path.join(TEST_DIR, directory))
        for filename in EXPECTED_FILES[directory]:
            assert os.path.exists(os.path.join(TEST_DIR, directory, filename))
    
    # Remove the test directory and files
    shutil.rmtree(TEST_DIR)
