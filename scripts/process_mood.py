from mood_file import read_mood_file


def get_wallpaper_path(mood):
    """
    Get wallpaper path from mood
    :param mood: user mood
    :return: wallpaper path
    """

    # Read the mood file
    config = read_mood_file()
    wallpaper_path_dict = config["Wallpapers"]

    # Check if mood exists
    if mood not in wallpaper_path_dict:
        print("Mood not found.")
        exit()

    # Get wallpaper path
    wallpaper_path = wallpaper_path_dict.get(mood)

    return wallpaper_path
