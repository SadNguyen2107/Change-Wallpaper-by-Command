from pathlib import Path
import subprocess
import json

# Get the home directory
home_dir = Path.home()

# Create a file in the home directory
file_path = home_dir / "mood.json"


def make_mood_file():
    """
    Create a mood.json in the home directory
    """

    # Create the file
    with open(file_path, "w") as file:
        file.write('{\n\t"Your mood here": "wallpaper path here"\n}')

    # Open VS Code and wait for the user to close it before continuing
    subprocess.run(
        [
            r"C:\Users\User\AppData\Local\Programs\Microsoft VS Code\Code.exe",
            "-w",
            str(file_path),
        ]
    )


def read_mood_file():
    with open(str(file_path), "r") as file:
        mood_to_wallpaper = json.load(file)
        
    print("\n".join(mood_to_wallpaper))