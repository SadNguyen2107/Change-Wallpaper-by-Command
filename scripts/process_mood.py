from pathlib import Path
import json


def get_wallpaper_path(mood):
    """
    Get wallpaper path from mood
    :param mood: user mood
    :return: wallpaper path
    """

    # Get the home directory
    home_dir = Path.home()

    # Create a file in the home directory
    file_path = home_dir / "mood.json"

    # Open the mood file
    with open(str(file_path), "r") as file:
        mood_to_wallpaper = json.load(file)

    # Get wallpaper path
    wallpaper_path = mood_to_wallpaper[mood]

    return wallpaper_path
