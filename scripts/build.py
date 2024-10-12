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
    
    # Define the path to the main script
    main_script = os.path.join(root_dir, 'main.py')  # Adjust this if your main script has a different name
    
    # Define additional data files to include
    assets_dir = os.path.join(root_dir, 'assets')
    
    # PyInstaller command line arguments
    args = [
        main_script,
        '--onefile',
        '--windowed',
        f'--add-data={assets_dir}{os.pathsep}assets',
        '--name=PixelatedShowdown',
    ]
    
    # Run PyInstaller
    PyInstaller.__main__.run(args)

if __name__ == "__main__":
    build_executable()
