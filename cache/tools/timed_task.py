import schedule
import time
from cache import tools
# 定义你要周期运行的函数
def job(name,name2):
    print("I'm working...",name,name2)
name = 'xiaoming'
name2 = 'xiao'
# schedule.every(10).minutes.do(job)               # 每隔 10 分钟运行一次 job 函数
# schedule.every().hour.do(job)                    # 每隔 1 小时运行一次 job 函数
# schedule.every().day.at("17:29").do(job)         # 每天在 10:30 时间点运行 job 函数
# schedule.every().monday.do(job)                  # 每周一 运行一次 job 函数
# schedule.every().wednesday.at("13:15").do(job)   # 每周三 13：15 时间点运行 job 函数
schedule.every().minute.at(":17").do(job,name,name2)        # 每分钟的 17 秒时间点运行 job 函数

while True:
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    schedule.run_pending()   # 运行所有可以运行的任务
    time.sleep(1)