import os
import subprocess

def run_pylint(file_path):
    """Run pylint on the given file and return the output."""
    result = subprocess.run(['pylint', file_path], capture_output=True, text=True)
    return result.stdout

def main():
    # Specify the directory containing the Python files you want to check
    directory = 'path/to/your/python/files'

    # Iterate over all files in the directory
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                print(f'Checking {file_path}...')
                pylint_output = run_pylint(file_path)
                print(pylint_output)

if __name__ == '__main__':
    main()