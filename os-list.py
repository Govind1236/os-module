import os
folder = os.listdir("Data")
for folders in folder :
    print(os.listdir(f"data/{folders}"))