import os

from google.genai import types


schema_get_files_info = types.FunctionDeclaration(
    name = "get_files_info",
    description = "Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters = types.Schema(
        type = types.Type.OBJECT,
        properties = {
            "directory": types.Schema(
                type = types.Type.STRING,
                description = "The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)


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
