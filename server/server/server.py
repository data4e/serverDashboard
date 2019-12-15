# coding=utf-8
import psutil
import json


def getServerInfo():

    result = {
        'cpu': {
            'physicalCores': psutil.cpu_count(),
            'logicalCores': psutil.cpu_count(logical=True),
            'usage': psutil.cpu_percent(interval=1)
        },
        'memory': {
            'total': psutil.virtual_memory().total / 1024 / 1024 / 1024,
            'used': psutil.virtual_memory().used / 1024 / 1024 / 1024
        },
        'disk': {
            'total': psutil.disk_usage("/").total / 1024 / 1024 / 1024,
            'used': psutil.disk_usage("/").used / 1024 / 1024 / 1024
        },
        'netWork': {
            'upLink': psutil.net_io_counters().bytes_sent / 1024,
            'down': psutil.net_io_counters().bytes_recv / 1024
        }
    }
    return json.dumps(result)