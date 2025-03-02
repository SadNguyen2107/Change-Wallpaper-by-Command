from input import get_user_input
from process_mood import get_wallpaper_path
from change_wallpaper import change_wallpaper

from mood_file import (
    is_mood_file_exist,
    print_mood_file,
    edit_mood_file,
    make_mood_file,
)

# Get user input
mood = get_user_input()

# Different commands for different moods
if mood == "-h" or mood == "--help" or mood == "":
    print(
        """
        Usage: mood [mood]

        Change your wallpaper based on your mood.

        Options:
        [mood]  Your current mood. If you want to see all the moods available, type `mood ls`.
        ls      List all the moods available.
        edit    Edit the mood file.
        """
    )
    exit()
elif not is_mood_file_exist():

    # Create a mood file
    make_mood_file()
    exit()

elif mood == "ls" or mood == "list":

    # Print all the moods current available
    print_mood_file()
    exit()

elif mood == "edit":

    # Open the file for the user to edit
    edit_mood_file()
    exit()

# If not the above commands, continue the process
# Process user mood
wallpaper_path = get_wallpaper_path(mood)

# Change wallpaper
change_wallpaper(wallpaper_path)
