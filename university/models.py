from django.db import models

class Graduate_school(models.Model):
    title = models.CharField(max_length=50, verbose_name="연구실 이름", null=True)
    major = models.CharField(max_length=20, null=True)
    professor = models.CharField(max_length=20, null=True)
    location = models.CharField(max_length=20, help_text="ㅇㅇ동 ㅇㅇㅇ호", null=True)
    telephone = models.CharField(max_length=11, null=True)
    url = models.URLField(blank=True, null=True)

class Quest(models.Model):
    name = models.CharField(max_length=100, null=True)
