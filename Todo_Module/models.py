from django.db import models

# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length = 200)
    content = models.TextField()
    priority = models.IntegerField(default = 1)
    is_done = models.BooleanField(default = False)

    def __str__(self):
        return f'{self.title} / Is_Done: {self.is_done}'

    class Meta:
        # Table name in db
        db_table = 'Todos'
