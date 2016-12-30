#!/usr/bin/env python
#-- coding: utf-8 --
import sys
import os
from imp import reload
import logging
import time
now = int(time.time())
timeArray = time.localtime(now)
otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
logging.basicConfig(level=logging.DEBUG,
                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                filename='myapp_new.log',
                filemode='w')

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
        f=os.system('sh /sh/restart_nginx.sh')
        return f

def CreateNginxConfigFile(project_type,project_name,domain_name,nginx_static_template,nginx_config_dir,index_fine,moblie_301_project_name,moblie_301_domain_name,second_level_domain,filename):
    try:
        if project_type=='other':
            #check mobile config
            if(os.path.exists(nginx_config_dir+project_name+'_mobile.conf')):
                #don do anything
                print(project_name+'allow ready has config')
                logging.info(project_name+'allow ready has config')
            else:
                f=open(nginx_config_dir+project_name+'_'+project_type+'.conf','w')
                n_template=open(nginx_static_template).read()
                n_content=n_template%(second_level_domain,project_name,domain_name,filename,filename,filename,index_fine)
                f.write(n_content)
                f.close()
        else:
            project_type='www'
            if(os.path.exists(nginx_config_dir+project_name+'_mobile.conf')):
                os.remove(nginx_config_dir+project_name+'_mobile.conf')
            f=open(nginx_config_dir+project_name+'_'+project_type+'.conf','w')
            n_template=open(nginx_static_template).read()
            n_content=n_template%(second_level_domain,moblie_301_project_name,moblie_301_domain_name,project_name,project_name,project_name,moblie_301_domain_name,index_fine,second_level_domain,project_name,domain_name,project_name,project_name,project_name,index_fine)
            f.write(n_content)
            f.close()
            if(os.path.exists(nginx_config_dir+project_name+'_www.conf')):
                os.remove(nginx_config_dir+project_name+'_www.conf')
        return project_name+"Success!"
    except f:
        return project_name+"Error to create nginx config file "

def UnzipSouceFile(source_file_path, destination_dir):
        try:
         os.system('unzip '+source_file_path+' -d '+destination_dir)
         return 'ok'
        except:
            return 'err'


