import os
import time
from subprocess import call, check_output, Popen, PIPE

path_to_watch = "./test_folder/"

before = dict([(f, os.stat(path_to_watch+f).st_mtime)
              for f in os.listdir(path_to_watch)])
dropbx = '/Users/hamidrezaomidvar/Desktop/Dropbox-Uploader/dropbox_uploader.sh'
# dropbx = '/home/users/homidvar/Dropbox-Uploader/dropbox_uploader.sh'


def check_file_busy(path_to_watch, f):
    lsout = Popen(['lsof', path_to_watch+f],
                  stdout=PIPE, shell=False)
    check_output(["grep", path_to_watch+f],
                stdin=lsout.stdout, shell=False)


def upload(dropbx,path_to_watch,f):
    bash_cmd = [dropbx, 'delete', '/'+f]
    call(bash_cmd, stdout=open(os.devnull, 'wb'))
    bash_cmd = [dropbx, 'upload', path_to_watch+f, '/']
    call(bash_cmd)

while 1:

    time.sleep(1)

    after = dict([(f, os.stat(path_to_watch+f).st_mtime)
                  for f in os.listdir(path_to_watch)])
    added = [f for f in after if not f in before]
    modified = [f for f in after if f in before
                and after[f] != before[f]]

    if added:
        for f in added:
            try:
              check_file_busy(path_to_watch, f)
              del after[f]
            except:
              print('Adding')
              upload(dropbx,path_to_watch,f)

    if modified:
        for f in modified:
            try:
                check_file_busy(path_to_watch, f)
                after[f] = -1
            except:
                print('Modifying')
                upload(dropbx,path_to_watch,f)

    before = after
