import os
import sys
from pathlib import Path

def main():
    # Change to the script's directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    
    # Debug information
    print("=== Debug Information ===")
    print(f"Script directory: {script_dir}")
    print(f"Current working directory: {os.getcwd()}")
    print("\nFiles in current directory:")
    for file in os.listdir():
        print(f"- {file}")
    print("\n=== File Check ===")
    
    # Check for required files
    print("Checking for required files...")
    required_files = ['start_server.py', 'form.html', 'combined_tiktok_data.json']
    missing_files = []
    
    for file in required_files:
        if not os.path.exists(file):
            missing_files.append(file)
            print(f"❌ Missing: {file}")
        else:
            print(f"✓ Found: {file}")
    
    if missing_files:
        print("\nError: Please make sure all these files are in the same folder as this script:")
        for file in missing_files:
            print(f"- {file}")
        return
    
    # Create PyInstaller spec file
    print("\nCreating spec file...")
    spec_content = """# -*- mode: python ; coding: utf-8 -*-

a = Analysis(
    ['start_server.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('form.html', '.'),
        ('combined_tiktok_data.json', '.')
    ],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False
)

pyz = PYZ(a.pure, a.zipped_data)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='VideoCodingApp',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None
)
"""
    spec_path = os.path.join(script_dir, 'VideoCodingApp.spec')
    with open(spec_path, 'w', encoding='utf-8') as f:
        f.write(spec_content)
    
    print("\nRunning PyInstaller...")
    os.chdir(script_dir)  # Ensure we're in the right directory
    os.system('pyinstaller --clean VideoCodingApp.spec')
    
    exe_name = "VideoCodingApp.exe" if os.name == 'nt' else "VideoCodingApp"
    exe_path = os.path.join(script_dir, 'dist', exe_name)
    if os.path.exists(exe_path):
        print(f"\n✓ Success! Your executable has been created in the 'dist' folder")
        print(f"✓ Location: {exe_path}")
    else:
        print("\n❌ Build failed. Please check the error messages above.")

if __name__ == '__main__':
    main()