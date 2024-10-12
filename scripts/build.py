#!/usr/bin/env python3
"""
Build script for creating executables of Pixelated Showdown.

This script uses PyInstaller to create standalone executables for
Windows and Linux platforms.
"""

import PyInstaller.__main__
import sys
import os

def build_executable():
    """Build the executable for the current platform."""
    # Determine the correct path separator based on the OS
    separator = '\\' if sys.platform.startswith('win') else '/'

    # Set the path to your main.py file
    main_file = f'src{separator}main.py'

    # Set the path to your assets folder
    assets_folder = f'assets{separator}'

    # PyInstaller command line arguments
    args = [
        main_file,
        '--onefile',
        '--windowed',
        f'--add-data={assets_folder}{separator}*{separator}assets{separator}',
        '--name=PixelatedShowdown',
        '--icon=assets/images/icon.ico',  # Make sure you have an icon file
    ]

    # Run PyInstaller
    PyInstaller.__main__.run(args)

if __name__ == "__main__":
    build_executable()
