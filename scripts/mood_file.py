from pathlib import Path
import subprocess
import configparser

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
    Open the mood.ini file for the user to edit
    """

    # VS Code path
    vs_code_path = (
        home_dir / "AppData" / "Local" / "Programs" / "Microsoft VS Code" / "Code.exe"
    )

    # Open VS Code and wait for the user to close it before continuing
    subprocess.run(
        [
            str(vs_code_path),
            "-w",
            str(file_path),
        ]
    )


def make_mood_file():
    """
    Create a mood.ini file in the home directory
    """

    config = configparser.ConfigParser()
    config["Wallpapers"] = {"Your mood here": "wallpaper path here"}

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

    if "Wallpapers" in config:
        moods = config["Wallpapers"]
        print("\n".join(moods))
    else:
        print("No wallpapers section found!")

    return config["Wallpapers"]
