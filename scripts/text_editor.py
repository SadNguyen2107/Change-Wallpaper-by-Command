import configparser

from mood_file import file_path

def get_text_editor():
    """
    Get the preferred text editor from mood.ini. Defaults to system editor if not set.
    """
    config = configparser.ConfigParser()
    config.read(file_path)

    return (
        config["Settings"].get("text_editor", "").strip()
        if "Settings" in config
        else ""
    )