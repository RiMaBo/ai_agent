import os
import subprocess


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
