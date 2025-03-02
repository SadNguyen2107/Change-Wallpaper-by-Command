mood_to_wallpaper = {
    "study": r"C:\Users\User\OneDrive - Hanoi University of Science and Technology\Pictures\Wallpapers\peakpx (1).jpg",
    "game": r"C:\Users\User\OneDrive - Hanoi University of Science and Technology\Pictures\Wallpapers\valorant-pc-games-2022-games-5k-8k-neon-typography-dark-3840x2160-8532.jpg",
    "waifu": r"C:\Users\User\OneDrive - Hanoi University of Science and Technology\Pictures\Wallpapers\miside-mita-dark-3840x2160-21051.jpg",
}

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