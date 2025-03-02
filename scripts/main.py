from input import get_user_input
from process_mood import get_wallpaper_path
from change_wallpaper import change_wallpaper

from mood_file import (
    make_mood_file, 
    read_mood_file,
    edit_mood_file,
)

# Get user input
mood = get_user_input()

# Different commands for different moods
if mood == "ls":

    # Print all the moods current available
    read_mood_file()
    exit()

elif mood == "config":

    # Open the file for the user to edit
    edit_mood_file()
    exit()

# If not the above commands, continue the process
# Process user mood
wallpaper_path = get_wallpaper_path(mood)

# Change wallpaper
change_wallpaper(wallpaper_path)
