# 1_mangaefile.py

# p.8
import os
import shutil

def list_text_file(folder_path):
    f_list = list()
    for file in os.listdir(folder_path):
        if file[-4:] == '.txt':
            f_list.append(file)
    return f_list

# folder = r"ch21\manage_file\folder1"
# print("1.txt 파일 목록:", list_text_file(folder))
# ['file1.txt', 'file2.txt', 'file3.bat', 'file4.csv']
# => ['file1.txt', 'file2.txt']
print("---------------------")
# p.9
import os
import shutil

def duplicate_text_file(folder_path, source_folder, destination_folder):
    f_list = list()
    for file in os.listdir(folder_path):
        if file[-4:] == '.txt':
            f_list.append(file)
    for file in f_list:
        src = os.path.join(source_folder, file)
        dst = os.path.join(destination_folder, file)
        shutil.copy(src, dst)
    return f_list

# folder = r"ch21\manage_file\folder1"
# src_folder = r"ch21\manage_file\folder1"
# dst_folder = r"ch21\manage_file\folder2"
# duplicate_text_file(folder, src_folder, dst_folder)

print("---------------------")
# p.10

def move_text_file(folder_path, source_folder, destination_folder):
    f_list = list()
    for file in os.listdir(folder_path):
        if file[-4:] == '.txt':
            f_list.append(file)
    for file in f_list:
        src = os.path.join(source_folder, file)
        dst = os.path.join(destination_folder, file)
        shutil.move(src, dst)
    return f_list

# folder = r"ch21\manage_file\folder1"
# src_folder = r"ch21\manage_file\folder1"
# dst_folder = r"ch21\manage_file\folder2"
# move_text_file(folder, src_folder, dst_folder)

print("---------------------")
# p.11

def remove_text_file(folder_path, destination_folder):
    f_list = list()
    for file in os.listdir(folder_path):
        if file[-4:] == '.txt':
            f_list.append(file)
    for file in f_list:
        dst = os.path.join(destination_folder, file)
        os.remove(dst)
    return f_list

# folder = r"ch21\manage_file\folder1"
# dst_folder = r"ch21\manage_file\folder2"
# remove_text_file(folder, dst_folder)