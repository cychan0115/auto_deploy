#!/usr/bin/env python
#-- coding: utf-8 --
import sys
import os
import time
import shutil
import main
from imp import reload
import logging
import time
now = int(time.time())
timeArray = time.localtime(now)
otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
logging.basicConfig(level=logging.DEBUG,
                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                filename='myapp_listen.log',
                filemode='w')

default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)
#############################################################################
#			Search source file control
#i will search deploy.todolist file
#if i found the deploy.todolist i will call my boday to check this
##############################################################################

source_dir='./source'
if os.path.exists(source_dir):
    print 'source dir config ok'
else:
    os.makedirs(source_dir)
print 'start.',
while 1:
  time.sleep(1)
  filelist=os.listdir(source_dir)
  configflie='null'
  for file1 in filelist:
   if file1[-9:] == '.zip.done'and file1[0:12] == 'Auto_Deploy_':
    print 'get start single..'
    logging.info('get start single..')
    os.remove('./source/'+file1)
    file1=file1[0:-5]
    print file1
    if os.path.exists('./source/'+file1):
        print file1
        print("start work")
        logging.info("start work")
        pname=file1[12:-4]
        if os.path.exists('./work'):
         shutil.rmtree('./work')
        os.makedirs('./work')
        shutil.move('./source/'+file1,'./work/')
        os.system('unzip ./work/'+file1 +' -d ./work/')
        #project_work_dir=myclass.unzipsoucefile('./work/'+file1,'./work/')
        configflie='./work/'+pname+'/config.xml'
        if main.main(configflie,'./work/'+file1,pname):
            shutil.rmtree('./work')
            os.makedirs('./work')
            #os.remove('./work/'+pname)#todo list on mac err permitted