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
#               update
#           1 mv the old source dir to rollback zoom
#           2 rename the dir to project_name+version
#           3 unzip new file
#############################################################################

def MakeRollbackDir(project_dir,rollbackdir,version):
    print ('  update  '+project_dir+'   to version ---->>  '+version)
    try:
        if os.path.exists(rollbackdir+'_version_'+str(int(version))):
            print('rollback dir exists del it ')
            shutil.rmtree(rollbackdir+'_version_'+str(int(version)))
            shutil.move(project_dir,rollbackdir+'_version_'+str(int(version)))
        else:
         shutil.move(project_dir,rollbackdir+'_version_'+str(int(version)))
    except shutil:
        return 'error'
    return 'success'

def UnzipSouceFile(source_file_path, destination_dir):
    destination_dir += '/'
    z = zipfile.ZipFile(source_file_path, 'r')
    try:
        for file in z.namelist():
            outfile_path = destination_dir + file
            if file.endswith('/'):
                os.makedirs(outfile_path)
            else:
                outfile = open(outfile_path, 'wb')
                outfile.write(z.read(file))
                outfile.close()
        z.close()

    except file:
        return 'error'
    return 'Success'
