import os

from google.genai import types


schema_write_file = types.FunctionDeclaration(
    name = "write_file",
    description = "Write a file with containing specified contents in the specified directory, constrained to the working directory.",
    parameters = types.Schema(
        type = types.Type.OBJECT,
        properties = {
            "file_path": types.Schema(
                type = types.Type.STRING,
                description = "The name of the file to write, relative to the working directory.",
            ),
            "content": types.Schema(
                type = types.Type.STRING,
                description = "The contents to write to the file.",
            ),
        },
        required=["file_path", "content"],
    ),
)


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
