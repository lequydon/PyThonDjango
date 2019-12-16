from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
class Theloai(models.Model):
    id = models.AutoField(primary_key=True)
    ten_the_loai=models.CharField(max_length=200)
class Tintuc(models.Model):
    id=models.AutoField(primary_key=True)
    tieu_de=models.CharField(max_length=1000)
    tom_tat=models.TextField(default={})
    hinh=models.ImageField(upload_to="images/", blank=True, null=True)
    ngaytao=models.DateTimeField(auto_now = True)
    noidung=RichTextField()
    theloai=models.ForeignKey(Theloai,on_delete=models.CASCADE)