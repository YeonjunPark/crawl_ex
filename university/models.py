from django.db import models

class Graduate_school(models.Model):
    title = models.CharField(max_length=50, verbose_name="연구실 이름")
    major = models.CharField(max_length=20, verbose_)
    professor = models.CharField(max_length=20)
    location = models.CharField(max_length=20, help="ㅇㅇ동 ㅇㅇㅇ호")
    telephone = models.IntegerField(max_length=11, validators=[])
    url = models.URLField(blank=True, null=True)


class Title(models.Model):
    title = models.CharField(max_length=100)