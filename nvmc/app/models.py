from django.db import models

class Create(models.Model):
    """新規作成モデル"""

    options = models.CharField(verbose_name = '選択', max_length= 5)
    