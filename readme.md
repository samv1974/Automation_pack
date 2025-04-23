# ⚙️ Python Automation Starter Pack  
A beginner-friendly set of Python automation scripts to boost your productivity by automating common day-to-day tasks.

---

### 1️⃣ Excel Formatter
**Function:**  
- Bolds the header row
- Auto-adjusts column widths
- Saves a new formatted file

**How to Use:**
1. Install `openpyxl`: `pip install openpyxl`
2. Place your `.xlsx` file in the same folder
3. Uncomment and update the file name in the last line of the script
4. Run: `python excel_formatter.py`



### 2️⃣ Bulk File Renamer
**Function:**
- Renames all files in a folder with a clean, consistent pattern.
- You choose the prefix (e.g., IMG_) and file type (e.g., .jpg).

**How to Use:**
1. Replace folder path in script with your actual folder.
2. Customize prefix and extension if needed.
3. Run the script: `python bulk_renamer.py`



### 3️⃣ PDF Merger  
**Function:**  
- Combines all PDF files in a folder into one single merged PDF.  
- Files are merged in alphabetical order.

**How to Use:**  
1. Install `PyPDF2`: `pip install PyPDF2`
1. Place all your PDF files in one folder.  
2. Replace the folder path in the script with your actual folder.  
3. Customize the output file name if needed.  
4. Run the script: `python pdf_merger.py`



### 4️⃣ Email Extractor  
**Function:**  
- Extracts all valid email addresses from a `.txt` file.  
- Saves the extracted, unique emails to a new text file.

**How to Use:**  
1. Place your input `.txt` file in the project folder.  
2. Replace the input and output file paths in the script.  
3. Run the script: `python email_extractor.py`


### 5️⃣ YouTube Video Downloader  
**Function:**  
- Downloads a YouTube video in the highest available resolution using a video URL.

**How to Use:**  
1. Install `pytube`: `pip install pytube`
1. Replace the video URL in the script with your desired YouTube link.  
2. Optionally change the download path if needed.  
3. Run the script: `python youtube_downloader.py`  


### 6️⃣ Instagram Profile Picture Downloader  
**Function:**  
- Downloads the profile picture of any public Instagram account.

**How to Use:**  
1. Install `instaloader`: `pip install instaloader`
1. Replace the username in the script with any public Instagram handle.  
2. Run the script: `python insta_dp_downloader.py`  
3. The profile picture will be saved in a folder named after the user.

### 📦 Install All Requirements
To install all dependencies at once, users can run:
`pip install -r requirements.txt`