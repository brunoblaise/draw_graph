"""
file to manage cronjobs in windows and writes to a file the day

file two to track the changes of the file the cronjobs are writing to and then loop over an image of 2d array and then generate commit according to it
"""
import datetime
#generate commit
KITTY = [
  [0, 0, 0, 4, 0, 0, 0],
  [0, 0, 4, 2, 4, 4, 4],
  [0, 0, 4, 2, 2, 2, 2],
  [2, 2, 4, 2, 4, 2, 2],
]  #image to loop over

"""
KITTY = [
  [0, 0, 0, 4, 0, 0, 0],
  [0, 0, 4, 2, 4, 4, 4],
  [0, 0, 4, 2, 2, 2, 2],
  [2, 2, 4, 2, 4, 2, 2],
]
"""

def generate_commit(image):
  commits = ""
  date = datetime.datetime.now()
  for week in image:
    for day in week:
      if day == 0:
        commits += " "
        continue
      elif day == 1:
        for i in range(3):
          commits += f"GIT_AUTHOR_DATE={date} GIT_COMMITTER_DATE={date} git commit --allow-empty -am 'Drawing'\n"
        continue
      elif day == 2:
        for i in range(6):
          commits += f"GIT_AUTHOR_DATE={date} GIT_COMMITTER_DATE={date} git commit --allow-empty -am 'Drawing'\n"
        continue
      elif day == 3:
        for i in range(12):
          commits += f"GIT_AUTHOR_DATE={date} GIT_COMMITTER_DATE={date} git commit --allow-empty -am 'Drawing'\n"
        continue
      elif day == 4:
        for i in range(24):
          commits += f"GIT_AUTHOR_DATE={date} GIT_COMMITTER_DATE={date} git commit --allow-empty -am 'Drawing'\n"
        continue
      else:
        commits += " "
      
  return commits


commits = generate_commit(KITTY)

with open('commits.sh', 'w') as f:
  f.write('#!/bin/bash\n')
  f.write(commits)
