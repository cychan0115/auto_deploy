#!/usr/bin/env python
#-- coding: utf-8 --
import sys
import os
import time
import shutil
import myclass
from imp import reload


default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)
from xml.dom import minidom
 #############################################################################
 #			read config from xml
 # this part is very suck will update in sometime
 ##############################################################################
def main(configfile):
 doc=minidom.parse(configfile)
 root=doc.documentElement
 projects=root.getElementsByTagName('porject')
 for project in projects:
  project_name=project.getElementsByTagName("name")[0].childNodes[0].nodeValue
  operation_type=project.getElementsByTagName("operation_type")[0].childNodes[0].nodeValue
  connect_email=project.getElementsByTagName("connect_email")[0].childNodes[0].nodeValue
  domain_name=project.getElementsByTagName("domain_name")[0].childNodes[0].nodeValue
  home_page=project.getElementsByTagName("home_page")[0].childNodes[0].nodeValue
  version=project.getElementsByTagName("version")[0].childNodes[0].nodeValue
  note=project.getElementsByTagName("note")[0].childNodes[0].nodeValue
  send_mail_address=project.getElementsByTagName("send_mail_address")[0].childNodes[0].nodeValue
  send_mail_host=project.getElementsByTagName("send_mail_host")[0].childNodes[0].nodeValue
  send_mail_name=project.getElementsByTagName( "send_mail_name" )[0 ].childNodes[0 ].nodeValue
  send_mail_pass=project.getElementsByTagName("send_mail_pass")[0].childNodes[0].nodeValue
  auto_config_path=project.getElementsByTagName("auto_config_path")[0].childNodes[0].nodeValue
  nginx_config_dir= project.getElementsByTagName("nginx_config_dir")[0].childNodes[0].nodeValue
  nginx_www_dir= project.getElementsByTagName("nginx_www_dir")[0].childNodes[0].nodeValue
  nginx_static_template=project.getElementsByTagName("nginx_static_template")[0].childNodes[0].nodeValue
  rollback_path=project.getElementsByTagName("rollback_path")[0].childNodes[0].nodeValue

 #############################################################################
 #			new project on line
 #############################################################################
 if operation_type == 'new':

  print('starting create.......')

  project_namezip='./source/'+project_name+".zip"

  import newproject

  if newproject.CreateNginxConfigFile(project_name,nginx_static_template):
   print('Create Nginx File is good')

  if newproject.UnzipSouceFile( project_namezip, nginx_www_dir ):
   print('Unzip Source File is good')

  if newproject.RestartNginx():
   print('Restart is good')
   import mail
   freeback=mail.pysendmail( send_mail_address , connect_email , operation_type , project_name , domain_name , send_mail_host , send_mail_name , send_mail_pass );
   print freeback
   #todo del the source file

 #############################################################################
 #			update project
 #############################################################################
 if operation_type == 'update':
  print('starting update.......')

  import updateproject
  if updateproject.makerollbackdir( nginx_www_dir + project_name , rollback_path+project_name , version ):
   print('make rollbak file done')

  project_namezip='./source/'+project_name+".zip"
  if updateproject.unzipsoucefile( project_namezip, nginx_www_dir ):
   print('Unzip Source File is good')
   import mail
   freeback=mail.pysendmail( send_mail_address , connect_email , operation_type , project_name , domain_name , send_mail_host , send_mail_name , send_mail_pass );
   print freeback
   #todo del the source file

 #############################################################################
 #			rollback project
 #############################################################################
 if operation_type == 'rollback':
  import rollback
  if rollback.Rollback( nginx_www_dir+project_name, rollback_path+project_name+ '_version_'+version ):
   print("Rollback success")
   import mail
   freeback=mail.pysendmail( send_mail_address , connect_email , operation_type , project_name , domain_name , send_mail_host , send_mail_name , send_mail_pass );
   print freeback
   #todo del the source file







