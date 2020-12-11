import psutil
import os
from termcolor import colored
import time
os.system('clear')
os.system('figlet CPU_INFO')
cpu_percent = psutil.cpu_percent(interval=1)
cpu_freq    = psutil.cpu_freq()
cpu_count = psutil.cpu_count()
cpu_time = psutil.cpu_times()
def print_detail():
    print (colored(('cpu_precent: ', cpu_percent),'green'))
    time.sleep(0.9)
    print (colored(('cpu_freq: ' ,cpu_freq),'green'))
    time.sleep(0.9)
    print (colored(('cpu_count: ' ,cpu_count),'green'))
    time.sleep(0.9)
    print (colored(('cpu_times: ' ,cpu_time),'green'))
    time.sleep(0.9)


print ('''

''')
print (colored('--Made by Ro706','yellow'))
print_detail()
