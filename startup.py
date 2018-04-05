import subprocess
import smtplib
import socket
from email.mime.text import MIMEText
import datetime

# Change to your own account information
to = 'ramconx@gmail.com'
gmail_user = 'XYZ@gmail.com'
gmail_password = 'XYZpass'
smtpserver = smtplib.SMTP('smtp.gmail.com', 587)
smtpserver.ehlo()
smtpserver.starttls()
smtpserver.ehlo
smtpserver.login(gmail_user, gmail_password)
today = datetime.date.today()

# internal ip, very linux specific
arg='ip route list'
p=subprocess.Popen(arg,shell=True,stdout=subprocess.PIPE)
data = p.communicate()
split_data = data[0].split()
ipaddr = split_data[split_data.index('src')+1]

#external ip
arg1='dig TXT +short o-o.myaddr.l.google.com @ns1.google.com'
p1=subprocess.Popen(arg1,shell=True,stdout=subprocess.PIPE)
data1 = p1.communicate()
#split_data1 = data1[0].split()
extipaddr = data1[0] #first entry of tuple
my_external_ip = 'Your external ip is %s' % extipaddr
my_ip = '\n Your ip is %s' %  ipaddr
msg = my_ip+my_external_ip
msg = MIMEText(msg)
msg['Subject'] = 'IP For RaspberryPi on %s' % today.strftime('%b %d %Y')
msg['From'] = gmail_user
msg['To'] = to
smtpserver.sendmail(gmail_user, [to], msg.as_string())
smtpserver.quit()
