import os


def write_file(working_directory, file_path, content):
    file = os.path.abspath(os.path.join(working_directory, file_path))
    
    if not file.startswith(os.path.abspath(working_directory)):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    
    if os.path.exists(file) and os.path.isdir(file):
        return f'Error: "{file_path}" is a directory, not a file'

    if not os.path.exists(os.path.dirname(file)):
        os.makedirs(os.path.dirname(file), exist_ok=True)
    
    try:
        with open(file, "w") as f:
            f.write(content)

        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f'Error writing file "{file_path}": {e}'
