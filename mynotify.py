import smtplib
from email.mime.text import MIMEText
from email.header import Header


def notify_email():
    with open("./result.txt") as f:
        msg = f.read()

    message = MIMEText(msg, 'plain', 'utf-8')

    subject = '执行完毕啦'
    message['Subject'] = Header(subject, 'utf-8')
    message['From'] = Header("林帅帅的AI", 'utf-8')
    message['To'] = Header("林帅帅", 'utf-8')

    from_addr = "18665847089@qq.com"
    password = ""
    smtp_server = "smtp.qq.com"
    to_addr = "linxinzhechn@foxmail.com"

    server = smtplib.SMTP_SSL(smtp_server, 465)  # SMTP协议默认端口是25
    server.set_debuglevel(1)
    server.login(from_addr, password)
    server.sendmail(from_addr, [to_addr], message.as_string())
    server.quit()
