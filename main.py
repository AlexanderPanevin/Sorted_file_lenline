import os
from pathlib import Path
# import pandas as pd

os.chdir('folder_user')

if os.path.isfile("sorted_file.txt"):
  os.remove("sorted_file.txt")

paths = sorted(Path('.').glob('*.txt'))
file_in_folder = list(map(str, paths))
# print(file_in_folder)

file_path_list = []
for file_name in file_in_folder:
  file_path = os.path.join(os.getcwd(), file_name) 
  file_path_list.append(file_path)
# print(file_path_list)

file_len_line = []
for file_path in file_path_list:
  with open(file_path, 'r', encoding='utf-8') as file_:
    file_lines = len(file_.readlines())
    file_len_line.append(file_lines)
# print(file_len_line)

data_file = []
for file_path in file_path_list:
  with open(file_path, 'r', encoding='utf-8') as file_:
    data = " ".join(file_.readlines())
    data_file.append(data)

new_list = [file_len_line] + [file_in_folder] + [data_file]
# print(new_list)

list_matrix_files =[list(i) for i in zip(*new_list)]
# print(list_matrix_files)

list_sorted =sorted(list_matrix_files)
for x in list_sorted:
    print(*x,'\n')
# df = pd.DataFrame(list_sorted)
# print(df)  

new_file = "sorted_file.txt"
with open(new_file, 'w', encoding='utf-8') as file_all:
  amount = int(len(list_sorted))
  for i in range(0,amount):
    file_all.write(str(list_sorted[i][1]) +'\n')
    file_all.write('Количество строк: ' + str(list_sorted[i][0]) + '\n\n')
    file_all.writelines(str(list_sorted[i][2]) + '\n\n')