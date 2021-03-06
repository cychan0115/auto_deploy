#!/usr/bin/env python
# -- coding: utf-8 --
import sys
import os
import re
from imp import reload
import logging
import time
import shutil
now = int(time.time())
timeArray = time.localtime(now)
otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
logging.basicConfig(level=logging.DEBUG,
                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                filename='myapp_main.log',
                filemode='w')

def getText ( node ) :
    if node.length == 0 :
        return None
    if node [ 0 ].childNodes.length == 0 :
        return None;
    return node [ 0 ].childNodes [ 0 ].nodeValue


default_encoding = 'utf-8'
if sys.getdefaultencoding ( ) != default_encoding :
    reload ( sys )
    sys.setdefaultencoding ( default_encoding )
from xml.dom import minidom


#############################################################################
#			read config from xml
# this part is very suck will update in sometime
##############################################################################
def main ( configfile , sourcefile ,filename ) :
    doc = minidom.parse ( configfile )
    root = doc.documentElement
    projects = root.getElementsByTagName ( 'project' )
    for project in projects :
        project_name = getText(project.getElementsByTagName ( "name" ))
        operation_type = getText(project.getElementsByTagName ( "operation_type" ))
        domain_name =  getText(project.getElementsByTagName ( "domain_name" ))
        if domain_name=='None':
            domain_name=project_name+'.com'
        project_type = getText(project.getElementsByTagName ( "project_type" ))
        moblie_301_domain_name =  getText(project.getElementsByTagName ( "moblie_301_domain_name" ))
        moblie_301_project_name =  getText(project.getElementsByTagName ( "moblie_301_project_name" ))
        version = getText(project.getElementsByTagName ( "version" ))
        second_level_domain=getText(project.getElementsByTagName ( "second_level_domain" ))
        # connect_email=project.getElementsByTagName("connect_email")[0].childNodes[0].nodeValue
        # note=project.getElementsByTagName("note")[0].childNodes[0].nodeValue
        # send_mail_address=project.getElementsByTagName("send_mail_address")[0].childNodes[0].nodeValue
        # send_mail_host=project.getElementsByTagName("send_mail_host")[0].childNodes[0].nodeValue
        # send_mail_name=project.getElementsByTagName( "send_mail_name" )[0 ].childNodes[0 ].nodeValue
        # send_mail_pass=project.getElementsByTagName("send_mail_pass")[0].childNodes[0].nodeValue
        # auto_config_path=project.getElementsByTagName("auto_config_path")[0].childNodes[0].nodeValue
        # nginx_config_dir= project.getElementsByTagName("nginx_config_dir")[0].childNodes[0].nodeValue
        nginx_config_dir = '/config/nginx/'
        # nginx_www_dir= project.getElementsByTagName("nginx_www_dir")[0].childNodes[0].nodeValue
        nginx_www_dir = '/data/www/auto_deploy/'
        # nginx_static_template_only_www=project.getElementsByTagName("nginx_static_template_only_www")[0].childNodes[0].nodeValue
        nginx_static_template_only_www = './template/nginx_conf1.txt'
        # nginx_static_template_301=project.getElementsByTagName("nginx_static_template_301")[0].childNodes[0].nodeValue
        nginx_static_template_301 = './template/nginx_conf2.txt'
        # rollback_path=project.getElementsByTagName("rollback_path")[0].childNodes[0].nodeValue
        rollback_path = '/data/rollback/'
        index_define='./'+getText(project.getElementsByTagName ( "index_path" ))
    try :
        #############################################################################
        #			new project on line
        #############################################################################
        if operation_type == 'update' :

            print('starting update ' + project_name + ' '+ project_type + '.......')
            logging.info('starting update ' + project_name +'   '+ project_type + '.......')

            import newproject

            if project_type == 'other' :
                nginx_static_template = nginx_static_template_only_www
                project_type_dir='www'
            if project_type == 'www' :
                nginx_static_template = nginx_static_template_301
                project_type_dir='mobile'

            if newproject.CreateNginxConfigFile ( project_type , project_name , domain_name , nginx_static_template ,
                                                  nginx_config_dir , index_define , moblie_301_project_name ,
                                                  moblie_301_domain_name,second_level_domain ,filename) :
                print('Create Nginx File is good')
                logging.info(project_name+'Create Nginx File is good')

            sourcefile2 = re.sub ( 'Auto_Deploy_(\w+).zip' , 'Auto_Deploy_\\1_' + project_type_dir + '.zip' , sourcefile )
            os.rename ( sourcefile , sourcefile2 )

            print('check dir exists '+nginx_www_dir+project_type_dir+'/'+filename)
            logging.info('check dir exists '+nginx_www_dir+project_type_dir+'/'+filename)
            if os.path.exists(nginx_www_dir+project_type_dir+'/'+filename):
                logging.info('move files to rollback')
                print('move files to rollback')
                if os.path.exists('/data/rollback/'+otherStyleTime+'_'+filename):
                    logging.info('dir exists! move file to rollback /data/rollback/'+otherStyleTime+'_'+filename+otherStyleTime)
                    print('move files to rollback++++')
                    os.rename ( '/data/rollback/'+otherStyleTime+'_'+filename , '/data/rollback/'+otherStyleTime+'_'+filename+otherStyleTime )
                shutil.move(nginx_www_dir+project_type_dir+'/'+filename,'/data/rollback/'+otherStyleTime+'_'+filename+otherStyleTime)
                logging.info('remove success!')
            else:
                logging.info('exists not ture')
                print('exists not ture')
            print('start unzip file')
            if newproject.UnzipSouceFile ( sourcefile2 , nginx_www_dir + project_type_dir ) :
                logging.info(project_name+'Unzip Source File is good')
                print(project_name+'Unzip Source File is good')
            else :
                 print(project_name+'Unzip Err!!')

            if newproject.RestartNginx ( ) :
                print(project_name+'Restart is good')
                logging.info(project_name+'Restart is good')

            import mail
            send_mail_address='cy.chen@networkgrand.com'
            connect_email='13926262295@139.com'
            send_mail_host='smtp.mxhichina.com'
            send_mail_name='cy.chen@networkgrand.com'
            send_mail_pass='123qwe!@#QWE!@#QWE'
            freeback = mail.pysendmail ( send_mail_address , connect_email , operation_type , project_name ,
                                         domain_name , send_mail_host , send_mail_name , send_mail_pass );
            print freeback
            connect_email='house.liu@networkgrand.com'
            freeback = mail.pysendmail ( send_mail_address , connect_email , operation_type , project_name ,
                                         domain_name , send_mail_host , send_mail_name , send_mail_pass );
            print freeback
            connect_email='bingyu.yue@networkgrand.com'
            freeback = mail.pysendmail ( send_mail_address , connect_email , operation_type , project_name ,
                                         domain_name , send_mail_host , send_mail_name , send_mail_pass );
            print freeback
            connect_email='cy.chen@networkgrand.com'
            freeback = mail.pysendmail ( send_mail_address , connect_email , operation_type , project_name ,
                                         domain_name , send_mail_host , send_mail_name , send_mail_pass );
            print freeback



        #############################################################################
        #			new project on line
        #############################################################################
        if operation_type == 'create' :

            print('starting create ' + project_name + ' '+ project_type + '.......')
            logging.info('starting create ' + project_name +'   '+ project_type + '.......')

            import newproject

            if project_type == 'other' :
                nginx_static_template = nginx_static_template_only_www
                project_type_dir='www'
            if project_type == 'www' :
                nginx_static_template = nginx_static_template_301
                project_type_dir='mobile'

            if newproject.CreateNginxConfigFile ( project_type , project_name , domain_name , nginx_static_template ,
                                                  nginx_config_dir , index_define , moblie_301_project_name ,
                                                  moblie_301_domain_name,second_level_domain ,filename) :
                print('Create Nginx File is good')
                logging.info(project_name+'Create Nginx File is good')

            sourcefile2 = re.sub ( 'Auto_Deploy_(\w+).zip' , 'Auto_Deploy_\\1_' + project_type_dir + '.zip' , sourcefile )
            os.rename ( sourcefile , sourcefile2 )

            if os.path.exists(nginx_www_dir+project_type_dir+'/'+filename):
                shutil.move(nginx_www_dir+project_type_dir+'/'+filename,'/data/rollback/'+otherStyleTime+'_'+filename)
            if newproject.UnzipSouceFile ( sourcefile2 , nginx_www_dir + project_type_dir ) :
                print(project_name+'Unzip Source File is good')
                logging.info(project_name+'Unzip Source File is good')
            else :
                print(project_name+'Unzip Err!!')
                logging.debug(project_name+'Unzip Err!!')

            if newproject.RestartNginx ( ) :
                print(project_name+'Restart is good')
                logging.info(project_name+'Restart is good')

            import mail
            send_mail_address='cy.chen@networkgrand.com'
            send_mail_host='smtp.mxhichina.com'
            send_mail_name='cy.chen@networkgrand.com'
            send_mail_pass='123qwe!@#QWE!@#QWE'
            connect_email='13926262295@139.com'
            freeback = mail.pysendmail ( send_mail_address , connect_email , operation_type , project_name ,
                                         domain_name , send_mail_host , send_mail_name , send_mail_pass );
            print freeback
            connect_email='house.liu@networkgrand.com'
            freeback = mail.pysendmail ( send_mail_address , connect_email , operation_type , project_name ,
                                         domain_name , send_mail_host , send_mail_name , send_mail_pass );
            print freeback
            connect_email='bingyu.yue@networkgrand.com'
            freeback = mail.pysendmail ( send_mail_address , connect_email , operation_type , project_name ,
                                         domain_name , send_mail_host , send_mail_name , send_mail_pass );
            print freeback
            connect_email='cy.chen@networkgrand.com'
            freeback = mail.pysendmail ( send_mail_address , connect_email , operation_type , project_name ,
                                         domain_name , send_mail_host , send_mail_name , send_mail_pass );
            print freeback

    except :
        logging.info('err')
        import mail
        send_mail_address='cy.chen@networkgrand.com'
        send_mail_host='smtp.mxhichina.com'
        send_mail_name='cy.chen@networkgrand.com'
        send_mail_pass='123qwe!@#QWE!@#QWE'
        connect_email='13926262295@139.com'
        mail.pysendmail ( send_mail_address , connect_email , 'err!!!' , project_name ,
                                         domain_name , send_mail_host , send_mail_name , send_mail_pass );
        return project_name+'err'

    return project_name+'success'
