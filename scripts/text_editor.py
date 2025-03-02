import configparser

from mood_file import file_path

### **🔥 Example Cases**
# | `text_editor` in `mood.ini`  | Behavior |
# |------------------------------|----------|
# | `C:\Program Files\Notepad++\notepad++.exe` | Opens Notepad++ |
# | `notepad.exe` | Opens Notepad (system default) |
# | `vim` (on Linux/macOS) | Opens Vim |
# | `subl` (if Sublime is installed) | Opens Sublime Text |
# | `invalid_path.exe` | Falls back to VS Code, then default editor |

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