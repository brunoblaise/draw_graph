#track the file change

import os
last_modified = os.stat("file.txt").st_mtime  
while True:
  if os.stat("file.txt").st_mtime != last_modified:
    print("File changed!")
