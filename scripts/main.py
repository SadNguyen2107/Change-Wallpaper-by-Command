from input import get_user_input
from process_mood import get_wallpaper_path
from change_wallpaper import change_wallpaper

# Get user input
mood = get_user_input()

# Process user mood
wallpaper_path = get_wallpaper_path(mood)

# Change wallpaper
change_wallpaper(wallpaper_path)