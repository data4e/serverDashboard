from django.db import models
from django.conf import settings

# Create your models here.


class BaseModel(models.Model):
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    update_time = models.DateTimeField('最后更新时间', auto_now=True)
    delete_flag = models.IntegerField(default=0, editable=False)
    create_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=True, verbose_name='创建人')

    class Meta:  # 抽象
        abstract = True
