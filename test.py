#upload file
import time
import commands
import os
import logging
import shutil
now = int(time.time())
timeArray = time.localtime(now)
otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
logging.basicConfig(level=logging.DEBUG,
                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                filename='myapp.log',
                filemode='w')
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
     logging.info('get start single..'+file1[:-5])
     re=commands.getoutput(cmd+file1[:-5]+' '+rsyncuser+'@'+server_ip+':'+server_dir)
     if re.find(err_text) == -1:
      re=commands.getoutput(cmd+file1+' '+rsyncuser+'@'+server_ip+':'+server_dir)
      if re.find(err_text)== -1:
       print 'success'
       logging.info('success''will del file '+file1+'will del file '+file1[:-5])
       if os.path.exists('/tmp/del'):
        print 'dir ok'
       else:
        os.mkdir('/tmp/del')
       shutil.move(file1,'/tmp/del/'+file1+otherStyleTime)
       shutil.move(file1[:-5],'/tmp/del/'+file1[:-5]+otherStyleTime)
     else:
      print 'err try again~~'
      logging.debug('err try again~~')
 time.sleep(3)
