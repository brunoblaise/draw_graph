
#cronjob in windows

import datetime

with open('file.txt', 'a') as File:
  File.write(f'{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n')

