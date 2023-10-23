from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

user = get_user_model()

class Todo(models.Model):
    title = models.CharField(max_length = 200)
    content = models.TextField()
    priority = models.IntegerField(default = 1)
    is_done = models.BooleanField(default = False)
    user = models.ForeignKey(to = user, on_delete = models.CASCADE, related_name = 'todos', blank = True, null = True )

    def __str__(self):
        return f'{self.title} / Is_Done: {self.is_done}'

    class Meta:
        # Table name in db
        db_table = 'Todos'
