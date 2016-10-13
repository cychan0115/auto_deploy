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
#               rollback
#           1 mv the old source dir to rollback zoom
#           2 rename the dir to project_name+version
#           3 unzip new file
#############################################################################