import os
import string 
def generating_alphabet_files(file_path):
    os.makedirs(file_path, exist_ok=True)

    for letters in string.ascii_uppercase:
        name_file=os.path.join(file_path, letters + ".txt")
        with open(name_file, "w") as zat:
            zat.write("London is the capital of Great Britan")

path="C:\\Users\\Aldo\\Desktop\\github.python\\python\\lab6"
generating_alphabet_files(path)