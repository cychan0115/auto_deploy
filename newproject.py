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

def UnzipSouceFile(project_name,unzip_path):
    unziptodir=unzip_path
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
                    shutil.move(p,p+now)
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

def RestartNginx(project_name):
    os.system('sh /sh/restart_nginx.sh')


