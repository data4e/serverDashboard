from django.db import models
from common.models import BaseModel
# Create your models here.


class Cpu(BaseModel):
    pass

    class Meta:
        db_table = 'sd_cpu'


class ServerInfo(BaseModel):
    # 服务器名称
    name = models.CharField('服务器名', max_length=32)
    desc = models.TextField('备注')
    score = models.IntegerField('核心数')

    class Meta:
        db_table = 'sd_server_info'
        verbose_name = '服务器信息'
        verbose_name_plural = '服务器信息'

    def __str__(self):
        return self.name
