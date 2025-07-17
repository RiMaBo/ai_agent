import os
import subprocess

from google.genai import types


schema_run_python_file = types.FunctionDeclaration(
    name = "run_python_file",
    description = "Runs a Python file in the specified directory, constrained to the working directory and returns the output.",
    parameters = types.Schema(
        type = types.Type.OBJECT,
        properties = {
            "file_path": types.Schema(
                type = types.Type.STRING,
                description = "The file to run, relative to the working directory.",
            ),
        },
        required=["file_path"],
    ),
)


def run_python_file(working_directory, file_path):
    file = os.path.abspath(os.path.join(working_directory, file_path))
    
    if not file.startswith(os.path.abspath(working_directory)):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.exists(file):
        return f'Error: File "{file_path}" not found.'

    if not os.path.splitext(file)[1] == ".py":
        return f'Error: "{file_path}" is not a Python file.'

    try:
        result = subprocess.run(["python3", file], capture_output=True, cwd=os.path.abspath(working_directory), timeout=30, text=True)
        if not result.returncode == 0:
            return f"Process exited with code {result.returncode}"
    
        if not len(result.stdout):
            return "No output produced."
    
        return f"STDOUT:\n{result.stdout}\nSTDERR:\n{result.stderr}"
    except Exception as e:
        return f'Error: executing Python file: {e}'
