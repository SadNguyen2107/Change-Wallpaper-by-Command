# Mood-Based Wallpaper Changer

A Python script that changes your wallpaper based on your mood.

## 🚀 Features

- Change wallpaper by specifying a mood.
- List available moods from the mood file.
- Edit the mood file directly.
- Automatically creates a mood file if it doesn't exist.

---

## 📦 Installation

### **1️⃣ Install Python**

Ensure you have **Python 3.6+** installed.  
Check by running:

```sh
python --version
```

### **2️⃣ Install Dependencies**

No external dependencies required.

---

## 🛠 Usage

### **Change directory**

```sh
cd scripts
```

### **Run the script**

```sh
python main.py <mood>
```

Example:

```sh
python main.py happy
```

### **List available moods**

```sh
python main.py ls
```

### **Edit the mood file**

```sh
python main.py edit
```

### **Show help**

```sh
python main.py -h
```

Or simply:

```sh
python main.py
```

---

## 📂 Folder Structure

```sh
project_root/
│-- scripts/
│   ├── main.py
│   ├── process_mood.py
│   ├── change_wallpaper.py
│   ├── mood_file.py
│-- bin/
│   ├── run_mood.ps1  # PowerShell script to run the program
│-- README.md
│-- LICENSE
```

---

## 🖥 PowerShell Usage

If using PowerShell, you can run:

```powershell
.\bin\run_mood.ps1 game
```

---

## 📝 How It Works

1. **Checks if the mood file exists** → If not, creates one.
2. **Processes the mood input**:
   - `"ls"` → Lists available moods.
   - `"edit"` → Opens mood file for editing.
   - `"-h"` → List all the commands available.
   - `<mood>` → Changes wallpaper accordingly.
3. **Changes the wallpaper** using the selected mood.

---

## 🎯 Example Mood File (`mood.ini`)

```ini
[Wallpapers]
happy = C:\Users\User\Pictures\happy.jpg
sad = C:\Users\User\Pictures\sad.jpg
excited = C:\Users\User\Pictures\excited.jpg

[Settings]
text_editor = C:\Program Files\Notepad++\notepad++.exe
```

---

## 📜 License

[MIT License](./LICENSE)

---

## 💡 Author

Developed by **@SadNguyen2107** 🚀
