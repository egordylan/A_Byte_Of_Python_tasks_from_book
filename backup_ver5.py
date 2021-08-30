import os, zipfile
import time


#  1. Files and directories to be copied are collected in a list.
#  A name containing spaces must be wrapped in double quotes.
source = ['D:\FreeCodeCamp\My Documents', 'D:\FreeCodeCamp\Code', 'D:\FreeCodeCamp\py4everyone', 'D:\FreeIT']

#  2. Backups should be stored in the primary backup directory.
target_dir = 'D:\FreeCodeCamp\Backup'

#  3. Files will place in zip-archive.
#  4. The current data serves as the name of a subdirectory in the main directory.
today = target_dir + os.sep + time.strftime('%Y%m%d')

#  For name of zip-archive serves current time.
now = time.strftime('%H%M%S')

#  Requesting user comment for file name.
comment = input('Input comment --> ')
if len(comment) == 0:  #  check if a comment has been entered
    target = today + os.sep + now + '.zip'
else:
    target = today + os.sep + now + '_' + \
             comment.replace(' ', '_') + '.zip'

#  Create a directory if it does not exist yet.
if not os.path.exists(today):
    os.mkdir(today)
    print('Directory successfully created', today)

print('Creating a new zip-file %s...' % target)
#  name of a directory + w write to archive + compression method
zip_File = zipfile.ZipFile(target, 'w', zipfile.ZIP_DEFLATED)

#  Traversing the entire directory tree and compressing files in each folder.
archDirName = ''

for sub_source in source:
    for dir, subdirs, files in os.walk(sub_source):
        print('Adding files from a directory %s...' % dir)
        #  Name of the current directory in the archive
        archDirName = ''.join(dir)
        #  Add current directory to archive
        zip_File.write(dir, archDirName)

        #  Adding files from the current directory to the archive
        for file in files:
            #  Name of the current file in the archive
            archFileName = dir + '/' + file
            zip_File.write(os.path.join(dir, file), archFileName)

zip_File.close()
print('The backup was successfully created in ', target)
