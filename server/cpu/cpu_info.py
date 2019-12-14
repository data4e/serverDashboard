# coding=utf-8
import psutil


class Cpu(object):
    def __init__(self):
        pass

    def cpu_info(self):
        print "--------------服务器信息查询------------------"

        print "CPU频率：" + psutil.cpu_freq().__str__()
        print "CPU逻辑核心数：" + psutil.cpu_count().__str__()
        print "CPU物理核心数：" + psutil.cpu_count(logical=False).__str__()
        print "CPU状态:" + psutil.cpu_stats().__str__()
        print psutil.cpu_percent()
        print psutil.cpu_times()
        print psutil.cpu_times_percent()

        swap = psutil.swap_memory()
        print "物理内存：" + (psutil.virtual_memory().total / 1024 / 1024 / 1024).__str__() + "GB"
        print "物理内存已使用：" + (psutil.virtual_memory().used / 1024 / 1024 / 1024).__str__() + "GB"

        print "交换区内存总量：" + (swap.total / 1024 / 1024 / 1024).__str__() + "GB"
        print "交换区内存已使用：" + (swap.used / 1024 / 1024 / 1024).__str__() + "GB"

        # t = Timer(5, cpu_info)
        # t.start()

        print "--------------服务器信息查询结束------------------"

    if __name__ == '__main__':
        cpu_info(self=1)
