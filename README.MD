# 🗂️ File Organizer Script in Python

A simple and beginner-friendly script written in **Python** that organizes files in a directory into categorized folders (e.g., Pictures, Documents, Videos, Music, etc.).

---

## 📌 Features

- Organizes files by extension:
  - 📷 Pictures (`.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp`)
  - 📄 Documents (`.pdf`, `.docx`, `.txt`, `.xlsx`)
  - 🎬 Videos (`.mp4`, `.mov`, `.avi`)
  - 🎵 Music (`.mp3`, `.wav`, `.aac`)
  - 🗜️ Archives (`.zip`, `.rar`, `.7z`)
  - 🗃️ Others (all uncategorized files)
- Option to:
  - Select a **specific directory** to organize
  - Organize the **current working directory**
- Automatically creates folders if they don't exist
- Summary report of the number of files moved
- Clear and interactive console prompts

---

## 📁 Project Structure

```
file-organizer-script/
├── main.py      # Main Python script
├── README.md    # Project documentation
└── LICENSE      # MIT License
```

---

## 🚀 How to Run

Make sure you have Python 3 installed on your system.

```bash
python main.py
```

You'll be prompted to select an option:
```
1. Organize a specific directory
2. Organize the current directory
```

Then the script will process and move your files into categorized folders.

---

## 🖥️ Example Usage

### ▶️ Option 1: Organize a Specific Directory

```
#############################################################################################
Welcome to the File Organizer Script!
This script organizes files into folders like Pictures, Documents, Videos, and more.

Choose an option to continue:
1. Organize a specific directory (Example: C:/Users/Luis Nava/Downloads)
2. Organize the current working directory (where this script is located)
#############################################################################################
Select an option (1 or 2): 1
Enter the full path of the folder to organize: C:/Users/Luis Nava/Downloads

Moved image1.png to Pictures
Moved resume.pdf to Documents
Moved song.mp3 to Music
Moved archive.zip to Archives

#############################################################################################
Total files moved to Documents: 1
Total files moved to Pictures: 1
Total files moved to Videos: 0
Total files moved to Music: 1
Total files moved to Archives: 1
Total files moved to Others: 0
#############################################################################################
Organized 4 files in 'C:/Users/Luis Nava/Downloads'.
#############################################################################################
```

---

### ▶️ Option 2: Organize the Current Working Directory

```
#############################################################################################
Welcome to the File Organizer Script!
This script organizes files into folders like Pictures, Documents, Videos, and more.

Choose an option to continue:
1. Organize a specific directory (Example: C:/Users/Luis Nava/Downloads)
2. Organize the current working directory (where this script is located)
#############################################################################################
Select an option (1 or 2): 2

Moved cat.jpg to Pictures
Moved homework.docx to Documents
Moved video.mp4 to Videos
Moved readme.txt to Documents
Moved unknownfile.xyz to Others

#############################################################################################
Total files moved to Documents: 2
Total files moved to Pictures: 1
Total files moved to Videos: 1
Total files moved to Music: 0
Total files moved to Archives: 0
Total files moved to Others: 1
#############################################################################################
Organized 5 files in 'C:/Users/LuisNava2001/file-organizer-script'.
#############################################################################################
```

---

## ✅ Requirements

- Python 3.x
- No external dependencies

---

## 👤 Author

### Luis Nava | [LuisNava2001](https://github.com/LuisNava2001)

> I'm exploring and sharing practical Python projects to simplify daily tasks.  
> Feel free to fork this repo, suggest improvements, or open issues!

---

## 📄 License

MIT License

