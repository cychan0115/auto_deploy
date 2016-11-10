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

def CreateNginxConfigFile(project_type,project_name,domain_name,nginx_static_template,nginx_config_dir,index_fine,moblie_301_project_name,moblie_301_domain_name):
    try:
        if project_type=='www':
            #check mobile config
            if(os.path.exists(nginx_config_dir+project_name+'_mobile.conf')):
                #don do anything
                print('allow ready has config')
            else:
                f=open(nginx_config_dir+project_name+'_'+project_type+'.conf','w')
                n_template=open(nginx_static_template).read()
                n_content=n_template%(project_name,domain_name,project_name,project_name,project_name,index_fine)
                f.write(n_content)
                f.close()
        else:
            project_type='mobile'
            if(os.path.exists(nginx_config_dir+project_name+'_mobile.conf')):
                os.remove(nginx_config_dir+project_name+'_mobile.conf')
            f=open(nginx_config_dir+project_name+'_'+project_type+'.conf','w')
            n_template=open(nginx_static_template).read()
            n_content=n_template%(moblie_301_project_name,moblie_301_domain_name,project_name,project_name,project_name,moblie_301_domain_name,index_fine,project_name,domain_name,project_name,project_name,project_name,index_fine)
            f.write(n_content)
            f.close()
            if(os.path.exists(nginx_config_dir+project_name+'_www.conf')):
                os.remove(nginx_config_dir+project_name+'_www.conf')
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



