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
#           0 check rollback version if exists
#           1 del www_dir project dir
#           2 cp version to www_dir
#############################################################################

def Rollback(del_www_dir,rollback_version_dir):
    if os.path.exists(rollback_version_dir):
        if os.path.exists(del_www_dir):
            shutil.rmtree(del_www_dir)
        shutil.copytree(rollback_version_dir,del_www_dir,True)

