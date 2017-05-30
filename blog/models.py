from django.db import models
from django.utils import timezone


# models for secs rank
class Secs(models.Model):
    sec_id = models.CharField(max_length=50, primary_key=True)
    sec_name = models.CharField(max_length=50, verbose_name='券商名称')
    gqj_data = models.CharField(max_length=50, verbose_name='成交额(亿)')
    gqj_rank = models.IntegerField(verbose_name='名次')

    def __str__(self):
        return self.sec_name


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200,verbose_name='标题')
    text = models.TextField(verbose_name='正文')
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True,verbose_name='更新时间')

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title