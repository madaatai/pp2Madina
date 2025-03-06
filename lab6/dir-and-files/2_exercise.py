import os
def checking_for_access(path):
    if not os.path.exists(path):
        print("Path doesn't exist")
        return
    else:
        print("Path does exist")
        print("Readable" if os.access(path, os.R_OK) else "Not readable")
        print("Writable" if os.access(path, os.W_OK) else "Not writable")
        print("Executable" if os.access(path, os.X_OK) else "Not executable")

path="C:\\Users\\Aldo\\Desktop\\github.python\\python\\lab6"
checking_for_access(path)