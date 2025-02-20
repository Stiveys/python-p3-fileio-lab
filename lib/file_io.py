# lib/file_io.py

def write_file(file_name, file_content):
    full_file_name = f"{file_name}.txt"
    with open(full_file_name, 'w') as f:
        f.write(file_content)

def append_file(file_name, append_content):
    full_file_name = f"{file_name}.txt"
    with open(full_file_name, 'a') as f:
        f.write(append_content)

def read_file(file_name):
    full_file_name = f"{file_name}.txt"
    with open(full_file_name, 'r') as f:
        return f.read()