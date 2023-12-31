# draw_graph


## Requirements
Everyday to commit 
Somedays to commit more messages than normal create a graph
#Able to deploy on other server
Commit message be days it running
Keep the commit message in a file before pushing.
Cronjobs

<br>
Windows task manager:
Every one hour -> write to a file

Python script check track changes in the file and if there is any commit 
<br>
## process
Create a 2d array of the image
Then create fake commit messages using of the 2d image array 

```

import os
from random import randint

for i in range(1, 9065):
    for j in range(0, randint(1, 10)):
     d = str(i) + ' days ago'
     with open('file.txt', 'a') as File:
            File.write(d)
    os.system('git commit -am "commit" ')

os.system('git push -u origin main')

```
