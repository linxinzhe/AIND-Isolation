import smtplib
from email.mime.text import MIMEText
from email.header import Header


def notify_email():
    with open("./tournament_result.txt") as f:
        msg = f.read()

    message = MIMEText(msg, 'plain', 'utf-8')

    subject = 'Program Done'
    message['Subject'] = Header(subject, 'utf-8')
    message['From'] = Header("Lin's AI", 'utf-8')
    message['To'] = Header("Xinzhe Lin", 'utf-8')

    from_addr = "sender@qq.com"
    password = ""
    smtp_server = "smtp.qq.com"
    to_addr = "receiver@qq.com"

    server = smtplib.SMTP_SSL(smtp_server, 465)  # SMTP协议默认端口是25
    server.set_debuglevel(1)
    server.login(from_addr, password)
    server.sendmail(from_addr, [to_addr], message.as_string())
    server.quit()
