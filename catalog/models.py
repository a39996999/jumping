from djongo import models

'''
class school(models.Model):
  name=models.CharField(max_length=20)
    
  class Meta:
    verbose_name = '學校資訊'
    verbose_name_plural = verbose_name
  def __str__(self):
    return self.name
'''
    
    
class student(models.Model):
  _id   = models.ObjectIdField()
  school= models.CharField(max_length=20, verbose_name='學校')
  item  = models.CharField(max_length=20, verbose_name='項目')
  group = models.CharField(max_length=20, verbose_name='組別')
  grade = models.CharField(max_length=20, verbose_name='年級')
  coach = models.CharField(max_length=20, verbose_name='指導老師')
  std_No=models.CharField(max_length=20, verbose_name='號碼')
  name  =models.CharField(max_length=20, verbose_name='姓名')
  score =models.IntegerField(verbose_name='次數',null=True)
  class Meta:
    ordering = ('-score',)
    verbose_name = '學生資訊'
    verbose_name_plural = verbose_name
  #def __str__(self):
  #  return self.std_No
# Create your models here.
