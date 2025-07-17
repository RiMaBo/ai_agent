import os
from google.genai import types

from config import *


schema_get_file_content = types.FunctionDeclaration(
    name = "get_file_content",
    description = f"Lists the contents of a file, up to {MAX_CHARS} characters, in the specified directory, constrained to the working directory.",
    parameters = types.Schema(
        type = types.Type.OBJECT,
        properties = {
            "file_path": types.Schema(
                type = types.Type.STRING,
                description = "The file to list the contents of, relative to the working directory.",
            ),
        },
        required=["file_path"],
    ),
)


def get_file_content(working_directory, file_path):
    file = os.path.abspath(os.path.join(working_directory, file_path))
    
    if not file.startswith(os.path.abspath(working_directory)):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.isfile(file):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    
    with open(file, "r") as f:
        file_content_string = f.read(MAX_CHARS)
    
    if os.path.getsize(file) > MAX_CHARS:
            file_content_string += f'[...File "{file_path}" truncated at 10000 characters]'
        
    return file_content_string
