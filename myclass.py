#!/usr/bin/env python
#-- coding: utf-8 --
import sys
import zipfile
import os
import time
import shutil
from imp import reload


default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)

#############################################################################
#       1 create a new nginx config file and make that work    CreateNginxConfigFile
#       2 move this file to nginx work path usually is /data/www/auto_depoly  UnzipSouceFile
#       3 create a v0.1 version by this case
#############################################################################

def containsAny(allstr,childstr):
  for c in allstr:
    if c in childstr: return True
  return False