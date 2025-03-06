import os

def list_of_files_and_directories(path="."):
    print(f"Contetnts of:{path}")

    print("Directories:")
    directories=[d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
    print(directories)

    print("Files:")
    files=[f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    print(files)

    print("Directories and Files:")
    alls=os.listdir(path)
    print(alls)

path="C:\\Users\\Aldo\\Desktop\\github.python\\python\\lab6"
list_of_files_and_directories(path)