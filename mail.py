#!/usr/bin/env python
#-- coding: utf-8 --
import sys
import os
default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)
#############################################################################
#			mail service
#
###
# sender = send_mail_address
# receivers = connect_email
# mail_template_file='report.txt'
# mail_type=success/error
##############################################################################
import smtplib
from email.mime.text import MIMEText
from email.header import Header
def pysendmail(sender,receivers,mail_type,project_name,domain_name):
	mail_host="smtp.mxhichina.com"  #设置服务器
	mail_user="cy.chen@networkgrand.com"    #用户名
	mail_pass="123qwe!@#QWE"   #口令
	mail_template_file='report.txt'


	mail_content=open(mail_template_file).read()
	body= mail_content%(project_name,project_name,domain_name,project_name)

	message = MIMEText(body, 'plain', 'utf-8')
	message['From'] = Header(sender, 'utf-8')
	message['To'] =  Header(receivers, 'utf-8')

	subject = "自动部署系统通知邮件----- "+project_name+'报告'
	message['Subject'] = Header(subject, 'utf-8')


	try:
		smtpObj = smtplib.SMTP(mail_host,25)
		smtpObj.login(mail_user,mail_pass)
		smtpObj.sendmail(sender, receivers, message.as_string())
		return "Success! to send "+receivers
	except smtplib.SMTPException:
		return "Error!!"