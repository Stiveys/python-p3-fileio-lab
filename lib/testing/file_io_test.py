# lib/testing/file_io_test.py

import pytest
from lib.file_io import write_file, append_file, read_file

def test_write_file(tmp_path):
    """Test write_file()"""
    file_name = tmp_path / "test_file"
    file_content = "This is a test content."
    write_file(file_name, file_content)
    with open(f'{file_name}.txt', 'r') as f:
        assert f.read() == file_content

def test_append_file(tmp_path):
    """Test append_file()"""
    file_name = tmp_path / "test_file"
    file_content = "This is a test content."
    append_content = "\nAppended content."
    write_file(file_name, file_content)
    append_file(file_name, append_content)
    with open(f'{file_name}.txt', 'r') as f:
        assert f.read() == file_content + append_content

def test_read_file(tmp_path):
    """Test read_file()"""
    file_name = tmp_path / "test_file"
    file_content = "This is a test content."
    write_file(file_name, file_content)
    file_content_read = read_file(file_name)
    assert file_content_read == file_content