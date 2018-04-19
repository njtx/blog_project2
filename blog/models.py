from django.db import models
from django.utils import timezone

class User(models.Model):
    name = models.CharField(max_length=50, verbose_name=u'用户名', unique=True)
    nickname = models.CharField(max_length=50, verbose_name=u'昵称', unique=True)
    password = models.CharField(max_length=50, verbose_name=u'密码')
    sex = models.CharField(max_length=2, choices=(('M', u'男'), ('F', u'女')), verbose_name='性别')
    email = models.CharField(max_length=30, null=True, blank=True, verbose_name='email')
    image = models.ImageField(upload_to='covers/%Y/%m/%D/', blank=True, null=True)
    create_time = models.DateTimeField(verbose_name='创建时间')
    update_time = models.DateTimeField(verbose_name='更新时间')

    class Meta:
        db_table = 'user'
        ordering=['-update_time']

    def __str__(self):
        return "%s,%s,%s" % (self.name, self.nickname, self.password)
    
    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.create_time = timezone.now()
        self.update_time = timezone.now()
        return super(User, self).save(*args, **kwargs)


