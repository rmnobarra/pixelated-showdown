#!/usr/bin/env python3
"""
Build script for creating executables of Pixelated Showdown.

This script uses PyInstaller to create standalone executables for
Windows and Linux platforms.
"""

import os
import sys
import PyInstaller.__main__

def build_executable():
    """Build the executable for the current platform."""
    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Get the root directory of the project (one level up from the script directory)
    root_dir = os.path.dirname(script_dir)
    
    # Print current directory and list files for debugging
    print(f"Current directory: {os.getcwd()}")
    print("Files in current directory:")
    for file in os.listdir():
        print(f"  {file}")
    
    print(f"\nRoot directory: {root_dir}")
    print("Files in root directory:")
    for file in os.listdir(root_dir):
        print(f"  {file}")
    
    # Try to find the main script
    main_script = None
    for file in os.listdir(root_dir):
        if file.endswith('.py') and file != 'setup.py':
            main_script = os.path.join(root_dir, file)
            break
    
    if not main_script:
        raise FileNotFoundError("Could not find a suitable main Python script.")
    
    print(f"\nUsing main script: {main_script}")
    
    # Define additional data files to include
    assets_dir = os.path.join(root_dir, 'assets')
    if not os.path.exists(assets_dir):
        print(f"Warning: Assets directory not found at {assets_dir}")
        assets_arg = []
    else:
        assets_arg = [f'--add-data={assets_dir}{os.pathsep}assets']
    
    # PyInstaller command line arguments
    args = [
        main_script,
        '--onefile',
        '--windowed',
        '--name=PixelatedShowdown',
    ] + assets_arg
    
    print(f"\nPyInstaller arguments: {args}")
    
    # Run PyInstaller
    PyInstaller.__main__.run(args)

if __name__ == "__main__":
    build_executable()
