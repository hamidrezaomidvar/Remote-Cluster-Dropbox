import os, time
from subprocess import call
path_to_watch = "."
before = dict ([(f, None) for f in os.listdir (path_to_watch)])
dropbx='/home/users/homidvar/Dropbox-Uploader/dropbox_uploader.sh'
while 1:
  time.sleep (2)
  after = dict ([(f, None) for f in os.listdir (path_to_watch)])
  added = [f for f in after if not f in before]
  removed = [f for f in before if not f in after]
  if added:
      for f in added:
          call([dropbx,'upload',f,'.'])	
  #if removed: print "Removed: ", ", ".join (removed)
  before = after
