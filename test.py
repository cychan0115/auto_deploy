#upload file
import time
import commands
import os

filedir='./'
rsyncuser='ng_static_dev'
server_ip='54.183.87.133'
cmd='rsync -Iv '
server_dir='/soft/auto_deploy/source/'
err_text='rsync error'
while 1:
 filelist=os.listdir(filedir)
 for file1 in filelist:
   if file1[-9:] == '.zip.done'and file1[0:12] == 'Auto_Deploy_':
    if os.path.exists(file1[:-5]):
     print 'get start single..'+file1[:-5]
     re=commands.getoutput(cmd+file1[:-5]+' '+rsyncuser+'@'+server_ip+':'+server_dir)
     if re.find(err_text) == -1:
      print re
      re=commands.getoutput(cmd+file1+' '+rsyncuser+'@'+server_ip+':'+server_dir)
      if re.find(err_text)== -1:
       print re
       print 'success'
       print 'will del file '+file1
       print 'will del file '+file1[:-5]
       #todo del file
     else:
      print 'err try again~~'
 time.sleep(3)
