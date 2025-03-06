import os
def check_path(path):
    if os.path.exists(path):
        print("Path exists")
        directory_name=os.path.dirname(path)
        print(f"Directory name:{directory_name}")
        file_name=os.path.basename(path)
        print(f"File name:{file_name}")
    else:
        print("Path doesn't exist")
        return
    
path="C:\\Users\\Aldo\\Desktop\\github.python\\python\\lab6"
check_path(path)