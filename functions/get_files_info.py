import os


def get_files_info(working_directory, directory=None):
    dir = os.path.abspath(working_directory)
    
    if directory:
        dir = os.path.abspath(os.path.join(working_directory, directory))
    
    if not dir.startswith(os.path.abspath(working_directory)):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    
    if not os.path.isdir(dir):
        return f'Error: "{directory}" is not a directory'
    
    output = []
    dirlist = os.listdir(dir)
    for file in dirlist:
        file_path = os.path.join(dir, file)
        file_size = os.path.getsize(file_path)
        file_isdir = os.path.isdir(file_path)
        output.append(f"- {file}: file_size={file_size}, is_dir={file_isdir}")
    
    return "\n".join(output)
