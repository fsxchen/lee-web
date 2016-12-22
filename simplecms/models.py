# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Product(models.Model):
    """
    the product
    """
    title = models.CharField(u'标题', max_length=200)
    online_image_url = models.CharField(u'外部图片的地址', max_length=512)
    image = models.ImageField('上传图片', upload_to='uploadImages')
    pub_date = models.DateTimeField('date published')

class About(models.Model):
    """
    about US
    """
    content = models.CharField(u'内容', max_length=1000)
# Create your models here.
