from pathlib import Path
import subprocess
import configparser

import os
import sys

# Get the home directory
home_dir = Path.home()

# Create a file in the home directory
file_path = home_dir / "mood.ini"


def is_mood_file_exist():
    """
    Check if the mood.json file exists
    """

    return file_path.exists()


def edit_mood_file():
    """
    Open the mood.ini file for the user to edit.
    First, try opening with VS Code. If it fails, open with the default editor.
    """

    from text_editor import get_text_editor
    editor_path = get_text_editor()

    if editor_path:
        try:
            subprocess.run([editor_path, str(file_path)], check=True)
            return  # Successfully opened with the preferred editor

        except (FileNotFoundError, subprocess.CalledProcessError):
            print(f"Failed to open with {editor_path}. Using default editor...")

    # Fallback to system default editor
    try:
        if sys.platform.startswith("win"):
            os.startfile(file_path)  # Windows

        elif sys.platform.startswith("darwin"):
            subprocess.run(["open", file_path])  # macOS

        else:
            subprocess.run(["xdg-open", file_path])  # Linux

    except Exception as e:
        print(f"Error opening file: {e}")


def make_mood_file():
    """
    Create a mood.ini file in the home directory
    """

    config = configparser.ConfigParser()
    config["Settings"] = {"text_editor": ""}
    config["Wallpapers"] = {"command_here": "wallpaper_path.jpg"}

    with open(file_path, "w") as file:
        config.write(file)

    # Open the file for the user to edit
    edit_mood_file()


def read_mood_file() -> dict["str"]:
    """
    Reads the mood.ini file and returns the stored moods.

    If the file does not exist, it creates one and prompts the user to edit it.

    :return: A dictionary containing mood-to-wallpaper mappings.
    """

    if not is_mood_file_exist():
        print("Mood file does not exist. Creating one now...")
        make_mood_file()

    config = configparser.ConfigParser()
    config.read(file_path)

    return config


def print_mood_file():
    """
    Print the mood.ini file contents
    :param config: mood.ini file contents
    """

    config = read_mood_file()

    if "Wallpapers" in config:
        moods = config["Wallpapers"]
        print("\n".join(moods))
    else:
        print("No wallpapers section found!")
