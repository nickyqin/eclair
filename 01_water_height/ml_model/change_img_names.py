# script to change the names of the pictures taken to "in" or "out" and the number
import os

dir = "new_img"

i = 1
for filename in os.listdir(dir):
    file = os.path.join(dir, filename)

    if i <= 24:
        os.rename(file, f"{dir}/out-{i:02d}.jpg")
    else:
        os.rename(file, f"{dir}/in-{i-24:02d}.jpg")
    
    i += 1