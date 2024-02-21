import os
if (not os.path.exists("Data")): 
   os.mkdir("Data")


for i in range(0, 100):
    os.rmdir(f"data/tutorial {i + 1}")
    # os.mkdir("data1")