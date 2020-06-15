#conding:utf-8
import smtplib
from email.mime.text import  MIMEText #导入MIMEText html模板
from email.mime.text import MIMENonMultipart  #导入附件模式发送模板
#1.参数配置
smtpserver="smtp.qq.com"#发件服务器
port=465#端口
sender="504527497@qq.com"#发件人
psw="tkyujpdduawmbgfc"  #授权码 QQ邮箱需要，其他不一定
receiver="504527497@qq.com"#收件人

#2.编写邮件html模板,读文件发送方法
with open("D:\\python\\common\\TestReport.html") as f:
    body=f.read()
#body='<pre><h1>测试报告，好屌<h1></pre>'
msg=MIMEText(body,'html','utf-8')
msg['from']=sender
msg['to']=receiver
msg['subject']  ="这是测试报告"

#3.发送邮件
smtp =smtplib.SMTP_SSL(smtpserver,port)
smtp.login(sender,psw)
smtp.sendmail(sender,receiver,msg.as_string())
smtp.quit()