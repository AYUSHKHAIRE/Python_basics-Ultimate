# https://docs.python.org/3/library/os.html 

import os

if(not os.path.exists("42_OS_modules/data")):
    os.mkdir('42_OS_modules/data')
#  creating folder


# for i in range(0,10):
#     os.mkdir(f"42_OS_modules/data/day{i+1}")
# created 10 folders !!!

# for i in range(0,3):
#     os.rename(f"42_OS_modules/data/tutorial{i+1}",f"42_OS_modules/data/tt{i+1}")
# renamed 3 folders !!!

# folders = os.listdir('42_OS_modules/data')
# for folder in folders:
#      print(folder)
#     # to see in folders
#      print(os.listdir(f"42_OS_modules/data/{folder}"))
#     # will tell about the files

# print(os.getcwd())
#  my working directory