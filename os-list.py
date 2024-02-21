import os
folder = os.listdir("Data")
# print(folder)
# print(os.getcwd())
for folders in folder :
    print(os.listdir(f"data/{folders}"))
