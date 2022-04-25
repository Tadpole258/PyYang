# 先导入相关的库和方法
import os
import email
import schedule
import time
import smtplib
import datetime
from email.mime.text import MIMEText  # 负责构造文本
from email.mime.image import MIMEImage  # 负责构造图片
from email.mime.multipart import MIMEMultipart  # 负责将多个对象集合起来
from email.header import Header
# os.chdir(r"E:\自动化邮件"), 设置发送邮件时附件文件存放的地址


def send_mail(subject_content, body_content, table_path,image_path):
    # 设置邮箱基本信息
    mail_host = "smtp.163.com"  # SMTP服务器,163邮箱。如果是QQ邮箱，163替换成qq
    mail_license = "AQIKUYITAVFOVRXH"  # 163邮箱授权码，如果是QQ授权码为:rpaihyeslhuubddg
    mail_sender = "evan0936@163.com"  # 发件人邮箱。550686230@qq.com
    mail_receivers = ["550686230@qq.com"]  # 收件人邮箱，可以为多个收件人
    # 构建MIMEMultipart对象代表邮件本身，可以往里面添加文本、图片、附件等
    mail = MIMEMultipart('related')


    # 设置邮件头部内容
    mail["From"] = "Yang<evan0936@163.com>"  # 发送者,注意规范格式
    mail["To"] = "QQ<550686230@qq.com>"  # 接受者,注意规范格式
    # 邮件主题

    mail["Subject"] = Header(subject_content,'utf-8')

    # 邮件正文内容

    # 构造文本,参数1：正文内容，参数2：文本格式，参数3：编码方式
    message_text = MIMEText(body_content,"plain","utf-8")
    # 向MIMEMultipart对象中添加文本对象
    mail.attach(message_text)


    # 添加附件(excel表格)
    tb_name = table_path.split('/')[-1]
    table = open(table_path, 'rb').read()
    atta = MIMEText(table, 'base64', 'utf-8')  # 构造附件
    cd_table = 'attachment; filename="{0}"'.format(tb_name)  # 设置附件文件名称
    atta["Content-Disposition"] = cd_table # 设置附件信息
    mail.attach(atta)  # 添加附件信息


    # 二进制读取图片

    cd_name = image_path.split('/')[-1]  # 获取文件名
    images = open(image_path,'rb')
    message_image = MIMEImage(images.read()) # 设置读取获取的二进制数据

    cd_image = 'attachment; filename="{0}"'.format(cd_name)  # 设置附件图片名称
    message_image["Content-Disposition"] = cd_image
    mail.attach(message_image) # 添加图片到邮件信息
    images.close() # 关闭刚才打开的文件


    # 发送邮件
    stp = smtplib.SMTP()  # 创建SMTP对象
    stp.connect(mail_host, 25)  # 发件人邮箱域名和端口，端口地址为25
    # stp.set_debuglevel(1)  # 可以打印出和SMTP服务器交互的所有信息，此处忽略
    stp.login(mail_sender,mail_license)  # 登录邮箱，传递参数1：邮箱地址，参数2：邮箱授权码
    # 发送邮件，传递参数1：发件人邮箱地址，参数2：收件人邮箱地址，参数3：把邮件内容格式改为str
    stp.sendmail(mail_sender, mail_receivers, mail.as_string())
    nowtime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(nowtime+", Sent Successfully!!!")
    stp.quit()  # 关闭SMTP对象


if __name__ == '__main__':
    subject_content = """Python邮件测试"""
    body_content = """
    Hello,
        这是一个测试邮件！

    Best Wished!
    Thanks
        """
    table_path = '../../algorithms/MachineLearning/2.LinearRegression/MLR-data.xlsx'
    image_path = 'cmongraphy.jpeg'
    # 每分钟的 17 秒时间点运行 job 函数
    schedule.every().minute.at(":17").do(send_mail,subject_content, body_content, table_path, image_path)
    while True:
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        schedule.run_pending()  # 运行所有可以运行的任务
        time.sleep(1)
