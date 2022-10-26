import os
import shutil

from_dir = r"C:\Users\jayad\OneDrive\Desktop\project102"
to_dir = r"C:\Users\jayad\OneDrive\Desktop\project102\document_files"

list_of_files = os.listdir(from_dir)
print(list_of_files)

for file_name in list_of_files :
    name, extension = os.path.splitext(file_name)
    print(name)
    print(extension)

    if extension == " ":
        continue
    if extension in ['.doc','.docx','.pdf','.txt']:
        path1 = from_dir +"/"+file_name
        path2= to_dir+"/"
        path3= to_dir+"/"+file_name
        print(path1)
        print(path2)
        print(path3)

        if os.path.exists(path2):
            print("moving files" + file_name + ".........")
            shutil.move(path1,path3)
        else:
            os.mkdir(path2)
            print("moving files" + file_name + ".........")
            shutil.move(path1,path3)


