from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length = 200, verbose_name = 'عنوان')
    text = models.TextField(blank = True)
    is_enable = models.BooleanField(default = False)
    publish_date = models.DateField(null = True, blank = True)
    created_date = models.DateTimeField(auto_now_add = True)
    updated_date = models.DateTimeField(auto_now = True)

    objects = models.Manager()

    def __str__(self):
        return self.title