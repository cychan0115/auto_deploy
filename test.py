#upload file
import time
import commands
import os

filedir='./'
rsyncuser='ng_static_dev'
while 1:
 filelist=os.listdir(filedir)
 for file1 in filelist:
   if file1[-9:] == '.zip.done'and file1[0:12] == 'Auto_Deploy_':
    if os.path.exists(file1[:-5]):
     print 'get start single..'+file1[:-5]
     re=commands.getoutput('rsync -vI --progress '+file1[:-5]+' '+rsyncuser+'@54.183.87.133:/soft/auto_deploy/source/')
     if re.find('rsync error') == -1:
      re=commands.getoutput('rsync -vI --progress '+file1+' '+rsyncuser+'@54.183.87.133:/soft/auto_deploy/source/')
      if re.find('rsync error')== -1:
       print 'success'
       #todo del file
     else:
      print 'err'
 time.sleep(2)
