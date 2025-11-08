import os

cwd=os.getcwd()
print("Current Working Diretory: ", cwd)
print("List Dir: ", os.listdir())

# Creating new Directory
new_dir = "demo_folder"
if not os.path.exists(new_dir):
    os.mkdir(new_dir)
    print(f"Created directory: ", new_dir)
    
# Rename Directory
rename_dir="rename_folder"
if not os.path.exists(rename_dir):
    os.rename(new_dir,rename_dir)
    print(f"Rename {new_dir} to {rename_dir}")
    
# Remove
os.rmdir(rename_dir)
print(f"Removed {rename_dir}")

# Home Directory Env variables
print(f"Home Dir: {os.getenv("HOME")}")