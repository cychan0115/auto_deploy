#!/usr/bin/env python
#-- coding: utf-8 --
import sys
import os
import time
import shutil
import myclass
import main
from imp import reload


default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)
from xml.dom import minidom
#############################################################################
#			Search source file control
#i will search deploy.todolist file
#if i found the deploy.todolist i will call my boday to check this
##############################################################################

source_dir='./source'
configflie='null'
while 1:
  print ("wait ....")
  time.sleep(1)
  filelist=os.listdir(source_dir)
  for file1 in filelist:
   if file1[-4:] == '.zip' and file1[0:12] == 'auto_deploy_':
    print file1
    print("start work")
    shutil.rmtree('./work')
    os.makedirs('./work')
    shutil.move('./source/'+file1,'./work/')
    project_work_dir=myclass.unzipsoucefile('./work/'+file1,'./work/')
    os.remove('./work/'+file1,)
    configflie=project_work_dir+'/config.xml'
    main.main(configflie)