#conding:utf-8
import smtplib
from email.mime.text import  MIMEText #导入MIMEText html模板
from email.mime.multipart import MIMEMultipart

#1.参数配置
smtpserver="smtp.qq.com"#发件服务器
port=465#端口
sender="504527497@qq.com"#发件人
psw="tkyujpdduawmbgfc"  #授权码 QQ邮箱需要，其他不一定
receiver="504527497@qq.com"#收件人

#2.编写邮件html模板,发送=附件方法
msg = MIMEMultipart()
msg['Subject']  ="这是测试报告"
msg['From']=sender
msg['To']=receiver
f=open("TestReport.html")
mail_body=f.read()
f.close()
#添加附件
att = MIMEText(mail_body,"base64", "utf-8")
att["Content-Type"] = "application/octet-stream"
att["Content-Disposition"] = 'attachment; filename="TestReport.html"'
msg.attach(att)
#加正文
body = MIMEText(mail_body,'html','utf-8')
msg.attach(body)


#3.发送邮件
smtp =smtplib.SMTP_SSL(smtpserver,port)
smtp.login(sender,psw)
smtp.sendmail(sender,receiver,msg.as_string())
smtp.quit()