from os import getcwd, listdir, mkdir, path, getenv
# import only perticular funcations to use not the entire module

cwd=getcwd() # just use function name no need to use os.getcwd()
print("Current Working Diretory: ", cwd)
print("List Dir: ", listdir())

# Creating new Directory
new_dir = "demo_folder"
if not path.exists(new_dir):
    mkdir(new_dir)
    print(f"Created directory: ", new_dir)
    

# Home Directory Env variables
print(f"Home Dir: {getenv("HOME")}")