'''
Backup a specific folder to destination folder
Modified the code from "A Byte of Python, 13.2"
'''

import sys
import os
import time

# Check argument
if len(sys.argv) == 1:
  print('Please input a source path')
  exit(1)

# Set a source and a desination
source = str(sys.argv[1])
target_dir = os.getcwd()+'/backup'
target = target_dir+os.sep+time.strftime('%Y%m%d_%H%M%S') + '.zip'

# Create a folder if the destination is not exist
if not os.path.exists(target_dir):
  os.mkdir(target_dir)
  
# Make a zip command
zip_command = 'zip -r {0} {1}'.format(target, source)

# Run the backup
print('Zip command is : ')
print(zip_command)
print('Running :')
if os.system(zip_command) == 0:
  print('Successful backup to', target)
else:
  print('Backup Failed')
