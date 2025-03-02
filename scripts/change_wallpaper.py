import ctypes


# Apply wallpaper
def change_wallpaper(wallpaper_path):
    try:
        ctypes.windll.user32.SystemParametersInfoW(20, 0, wallpaper_path, 3)

    except Exception as e:
        print(f"Error: {e}")
