# coding=utf-8
import psutil
import json


def getServerInfo():
    # 获取CPU信息
    print psutil.cpu_count()     # 逻辑核心数
    print psutil.cpu_stats()
    print psutil.cpu_count(logical=True)    # CPU 物理核心数
    print psutil.cpu_times()    # 统计CPU的用户／系统／空闲时间：
    print psutil.cpu_percent(interval=1, percpu=True)

    # 获取内存信息
    print psutil.virtual_memory()  # 物理内存
    print psutil.swap_memory()  # 交换内存

    # 磁盘信息
    print psutil.disk_partitions()
    print psutil.disk_usage("/")
    print psutil.disk_io_counters()

    # 网络信息
    print psutil.net_io_counters()
    print psutil.net_if_addrs()
    

if __name__ == '__main__':
    getServerInfo()