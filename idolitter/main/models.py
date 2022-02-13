from django.db import models

class Group(models.Model):
  """アイドルグループモデル"""
  class Meta:
    db_table = 'group'
  
  name = models.CharField(verbose_name='グループ名', max_length=255, unique=True)
  twitterUsername = models.CharField(verbose_name='Twitter Username', max_length=15)
  twitterId = models.CharField(verbose_name='Twitter ID', max_length=20, null=True)
  twitterName = models.CharField(verbose_name='Twitter Name', max_length=50, null=True)
  twitterDescription = models.TextField(verbose_name='Twitter Description', null=True)

  def __str__(self):
    return self.name

class Idol(models.Model):
  """アイドルモデル"""
  class Meta:
    db_table = 'idol'

  group = models.ManyToManyField(Group, verbose_name='グループ名')
  name = models.CharField(verbose_name='名前', max_length=255, unique=True)
  twitterUsername = models.CharField(verbose_name='Twitter Username', max_length=15)
  twitterId = models.CharField(verbose_name='Twitter ID', max_length=20, null=True)
  twitterName = models.CharField(verbose_name='Twitter Name', max_length=50, null=True)
  twitterDescription = models.TextField(verbose_name='Twitter Description', null=True)

  def __str__(self):
    return self.name