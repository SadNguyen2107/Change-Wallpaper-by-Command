import ctypes

# Path to the wallpaper image
wallpaper_path = r"C:\Users\User\OneDrive - Hanoi University of Science and Technology\Pictures\Wallpapers\peakpx (1).jpg"

# Apply wallpaper   
SPI_SETDESKWALLPAPER = 20
ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, wallpaper_path, 3)


