from input import get_user_input
from process_mood import mood_to_wallpaper

# Get user input
mood = get_user_input()

# Process user mood
wallpaper_path = mood_to_wallpaper[mood]