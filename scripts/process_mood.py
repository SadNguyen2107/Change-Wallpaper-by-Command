from mood_file import (
    read_mood_file,
)


def get_wallpaper_path(mood):
    """
    Get wallpaper path from mood
    :param mood: user mood
    :return: wallpaper path
    """

    # Read the mood file
    wallpaper_path_dict = read_mood_file()

    # Get wallpaper path
    wallpaper_path = wallpaper_path_dict.get(mood)

    return wallpaper_path
