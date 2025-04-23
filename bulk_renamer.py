import os

def bulk_rename(folder_path, prefix="File", extension="jpg"):
    files = os.listdir(folder_path) 
    files = [f for f in files if f.endswith(f".{extension}")]
    files.sort()

    for i, filename in enumerate(files, start=1):
        new_name = f"{prefix}_{str(i).zfill(3)}.{extension}"
        src = os.path.join(folder_path, filename)
        dst = os.path.join(folder_path, new_name)
        os.rename(src, dst)

    print(f"Renamed {len(files)} files in {folder_path}!")

# Example usage
# bulk_rename("path of your folder containing photos", prefix="IMG", extension="jpg")
