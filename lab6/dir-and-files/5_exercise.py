def write_list_file(file_path, data_path):
    try:
        with open(file_path, 'w') as zat:
            for item in data_path:
                zat.write(str(item)+"\n")
        print("List written !")
    except:
        print("Error")

data=["Apple", "Banana", "Cherry", "12345", "loool"]
file="C:\\Users\\Aldo\\Desktop\\github.python\\python\\lab6\\zat.txt"
write_list_file(file, data)