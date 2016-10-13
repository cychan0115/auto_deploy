#!/usr/bin/env python
#-- coding: utf-8 --
import sys
import os
from imp import reload


default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)
from xml.dom import minidom
#############################################################################
#			Search source file control
#i will search deploy.todolist file
#if i found the deploy.todolist i will call my boday to check this todo list
##############################################################################
filename='test.xml'
config_path='./config/'
nginx_config='/config/nginx/'
www_path= '/data/www/auto_deploy/'
rollback_path='/data/rollback/'
configflie=config_path+filename


if os.path.isfile(configflie):
 print ("Config file OK ")
else:
 print ("False can't find config file")
 sys.exit("Sorry, goodbye!")


#############################################################################
#			test
# <?xml version="1.0" encoding="UTF-8"?>
# <response>
#     <porject>
#       <name>test1</name>
#       <operation_type>new</operation_type>
#       <connect_email>jd_chen@139.com</connect_email>
#       <send_mail_address>cy.chen@networkgrand.com</send_mail_address>
#       <domain_name>test1.com</domain_name>
#       <home_page>index.html</home_page>
#       <version>0.1</version>
#       <note>remark something</note>
#     </porject>
# </response>
###default sub domain project_name.networkgrand.com
##############################################################################
#todo
# import config
# project_name=config.
#######################################

#############################################################################
#			read config from xml
#
###
# sender = send_mail_address
# receivers = connect_email
# mail_template_file='report.txt'
# mail_type=success/error
# print "project_name="+project_name
# print "operation_type="+operation_type
# print "connect_email="+connect_email
# print "domain_name="+domain_name
# print "home_page="+home_page
# print "version="+version
# print "note="+note
# print "send_mail_address="+send_mail_address
# this part is very suck will update in sometime
##############################################################################

doc=minidom.parse(configflie)
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


#############################################################################
#			new project on line
#############################################################################
if operation_type == 'new':

 print('starting create.......')

 project_namezip='./source/'+project_name+".zip"

 import newproject

 if newproject.CreateNginxConfigFile(project_name):
  print('Create Nginx File is good')

 if newproject.UnzipSouceFile(project_namezip, www_path ):
  print('Unzip Source File is good')

 if newproject.RestartNginx():
  print('Restart is good')

#############################################################################
#			update project
#############################################################################
if operation_type == 'update':
 print('starting update.......')

 import updateproject

 if updateproject.MakeRollbackDir( www_path + project_name , rollback_path+project_name , version ):
  print('make rollbak file done')

 project_namezip='./source/'+project_name+".zip"
 if updateproject.UnzipSouceFile( project_namezip, www_path ):
  print('Unzip Source File is good')
  #todo del the source file

#############################################################################
#			rollback project
#############################################################################
if operation_type == 'rollback':
 print ('hello')

#############################################################################
#			send mail
#############################################################################
# import mail
# freeback=mail.pysendmail(send_mail_address,connect_email,"new",project_name,domain_name);
# print freeback






