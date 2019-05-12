import os
import time
from subprocess import call

path_to_watch = "./test_folder/"

before = dict([(f, os.stat(path_to_watch+f).st_mtime)
              for f in os.listdir(path_to_watch)])
#dropbx = '/Users/hamidrezaomidvar/Desktop/Dropbox-Uploader/dropbox_uploader.sh'
dropbx = '/Users/hamidrezaomidvar/Desktop/Dropbox-Uploader/dropbox_uploader.sh'

while 1:

    time.sleep(2)

    after = dict([(f, os.stat(path_to_watch+f).st_mtime)
                  for f in os.listdir(path_to_watch)])

    added = [f for f in after if not f in before]

    modified = [f for f in after if f in before
                and after[f] != before[f]]

    if added:
        for f in added:
            bash_cmd = [dropbx, 'upload', path_to_watch+f, '/']
            call(bash_cmd)

    if modified:
        for f in modified:
            print(os.stat(path_to_watch+f).st_mtime)
            bash_cmd = [dropbx, 'upload', path_to_watch+f, '/']
            call(bash_cmd)

    before = after
