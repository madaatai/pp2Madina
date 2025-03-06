import os

def copier():
    original_file = input("Enter the name of the file: ").strip()

    if not os.path.exists(original_file):
        print("Error file not found!")
        return

    lab6_folder = "C:\\Users\\Aldo\\Desktop\\github.python\\python\\lab6"
    os.makedirs(lab6_folder, exist_ok=True)

    with open(original_file, 'r') as file:
        data = file.read()

    filename = os.path.basename(original_file)
    if "." in filename:
        name, ext = filename.rsplit(".", 1)
        copy_name = f"{name}_1.{ext}"
    else:
        copy_name = filename + "_1"

    copy_path = os.path.join(lab6_folder, copy_name)

    with open(copy_path, "w") as file_copy:
        file_copy.write(data)

    print(f"File copied successfully to: {copy_path}")

copier()