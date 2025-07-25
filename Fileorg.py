import os
import shutil

source = r"C:\Users\92420\Downloads"
my_folder = r"E:\Gokul\Gokul resigning docs\Gokul docs" 

personal_names = ["resume", "Resume", "Gokul", "gokul" ]


def fileorg(source):
    Files_moved = 0
    for file in os.listdir(source):
        file_path = os.path.join(source, file)

        if os.path.isfile(file_path):
            file_lower = file.lower()
        
        if any(keyword in file_lower for keyword in personal_names):
            os.makedirs("Gokul resume", exist_ok=True)
            shutil.move(file_path, my_folder)
            Files_moved += 1
    print(Files_moved)
    print(my_folder)
fileorg(source)

