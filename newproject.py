#!/usr/bin/env python
#-- coding: utf-8 --
import sys
import zipfile
import os
import time
import shutil
import myclass
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
def RestartNginx():
    try:
        f=os.system('sh ./script/restart_nginx.sh')
    except f:
        return f
    return f

def CreateNginxConfigFile(project_name):
    try:
        nginx_static_template='./template/nginx_conf.txt'
        nginx_conf_path='/config/nginx/'
        f=open(nginx_conf_path+project_name+'.conf','w')
        n_template=open(nginx_static_template).read()
        n_content=n_template%(project_name,project_name,project_name,project_name,'index.html')
        f.write(n_content)
        f.close()
        return "Success!"
    except f:
        return "Error to create nginx config file "

def UnzipSouceFile(source_file_path, destination_dir):
    if os.path.exists(destination_dir):
        shutil.rmtree(destination_dir)
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



