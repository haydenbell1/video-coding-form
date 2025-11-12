import os
import sys
import shutil
from pathlib import Path

def create_build_script():
    # Get absolute path of current directory
    current_dir = os.path.abspath(os.path.dirname(__file__))
    
    # Create the build script with proper string formatting
    build_script = '''
import PyInstaller.__main__
import os
import shutil
import sys
from pathlib import Path

# Get the current directory
current_dir = Path(__file__).parent.absolute()

def check_required_files():
    required_files = ['start_server.py', 'form.html', 'combined_tiktok_data.json']
    missing_files = []
    
    for file in required_files:
        if not os.path.exists(os.path.join(current_dir, file)):
            missing_files.append(file)
    
    if missing_files:
        print("Error: The following required files are missing:")
        for file in missing_files:
            print(f"- {file}")
        sys.exit(1)

def build_app():
    # Check for required files first
    check_required_files()
    
    # Get absolute paths
    start_server_path = os.path.join(current_dir, 'start_server.py')
    form_html_path = os.path.join(current_dir, 'form.html')
    data_json_path = os.path.join(current_dir, 'combined_tiktok_data.json')
    
    # Define the separator based on OS
    separator = ";" if os.name == 'nt' else ":"
    
    # Create PyInstaller command
    command = [
        start_server_path,
        '--name=VideoCodingApp',
        '--onefile',
        '--add-data', f'{form_html_path}{separator}.',
        '--add-data', f'{data_json_path}{separator}.',
        '--clean'
    ]
    
    # Run PyInstaller
    print("Starting build process...")
    print(f"Using files from: {current_dir}")
    PyInstaller.__main__.run(command)
    
    print("\\nBuild completed! The executable is in the 'dist' folder.")
    
    # Verify the build
    exe_name = "VideoCodingApp.exe" if os.name == 'nt' else "VideoCodingApp"
    exe_path = os.path.join(current_dir, 'dist', exe_name)
    
    if os.path.exists(exe_path):
        print(f"Successfully created: {exe_path}")
    else:
        print("Warning: Executable was not created as expected")

if __name__ == '__main__':
    build_app()
'''
    
    # Write the build script to a file
    with open('build_app.py', 'w') as f:
        f.write(build_script.strip())

def create_requirements():
    # Create requirements.txt
    requirements = """
pyinstaller==6.3.0
"""
    with open('requirements.txt', 'w') as f:
        f.write(requirements.strip())

def create_readme():
    # Create README.md
    readme = """
# Video Coding Application

## Setup Instructions

1. Make sure you have all these files in the same directory:
   - start_server.py
   - form.html
   - combined_tiktok_data.json
   - build_app.py
   - requirements.txt

2. Install Python 3.8 or newer if you haven't already

3. Open a terminal/command prompt in this directory

4. Run these commands:
   ```
   pip install -r requirements.txt
   python build_app.py
   ```

5. Find the executable in the `dist` folder

## Usage

Simply double-click the VideoCodingApp executable in the dist folder. This will:
1. Start a local web server
2. Open your default web browser to the coding form
3. Allow you to code videos and save your progress

## Notes

- Keep the executable in the same folder as your data file
- The server runs locally on your machine
- Close the console window to shut down the server when you're done
"""
    with open('README.md', 'w') as f:
        f.write(readme.strip())

def verify_files():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    required_files = ['start_server.py', 'form.html', 'combined_tiktok_data.json']
    missing_files = []
    
    print("Checking for required files...")
    for file in required_files:
        file_path = os.path.join(current_dir, file)
        if not os.path.exists(file_path):
            missing_files.append(file)
            print(f"Missing: {file}")
        else:
            print(f"Found: {file}")
    
    return missing_files

if __name__ == '__main__':
    # First verify all required files are present
    missing_files = verify_files()
    
    if missing_files:
        print("\nError: Some required files are missing. Please ensure these files are in the same directory:")
        for file in missing_files:
            print(f"- {file}")
        print("\nCannot continue with setup until all files are present.")
        sys.exit(1)
    
    # Create all necessary files
    create_build_script()
    create_requirements()
    create_readme()
    
    print("\nSetup files created successfully!")
    print("\nTo build the application:")
    print("1. Install requirements: pip install -r requirements.txt")
    print("2. Run the build script: python build_app.py")
    print("3. Find the executable in the 'dist' folder")