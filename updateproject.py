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
#           1 mv the old file to rollback zoom
#           2 unzip source file
#############################################################################
def UnzipSouceFile(project_name,unzip_path,version):
    unziptodir=unzip_path
    oldversion=int(version)-1
    zipfilename='./source/'+project_name+'.zip'
    try:
        if not os.path.exists(unziptodir):
            os.mkdir(unziptodir, 0777)
        zfobj = zipfile.ZipFile(zipfilename)
        for name in zfobj.namelist():
            name = name.replace('\\','/')

            if name.endswith('/'):
                p = os.path.join(unziptodir, name[:-1])
                if os.path.exists(p):
                    now=time.strftime("%Y%m%d%H%M")
                    shutil.move(p,p+oldversion)
            else:
                ext_filename = os.path.join(unziptodir, name)
                ext_dir= os.path.dirname(ext_filename)
                if not os.path.exists(ext_dir):
                    os.mkdir(ext_dir,0777)
                outfile = open(ext_filename, 'wb')
                outfile.write(zfobj.read(name))
                outfile.close()
        return "success"
    except zfobj:
        return 'error'

