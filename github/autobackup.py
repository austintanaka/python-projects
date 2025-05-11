import os.path
import shutil

data = []
source =  input("please input the data yuo want to back up")
destination = input("please input the destination the data you wan to backup")

while True:
   if os.path.isdir(source):
       shutil.copytree(source,destination)

   else:
       shutil.copy(source,destination)
       print("success to back up the data")

    shutil.make_archive(source, "zip", destination)
    data.append(f"{source} turn ito zip back up into {destination}")

