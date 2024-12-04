from django.db import models
from user.models import User

class Student(models.Model):
    name = models.CharField(max_length = 50)
    user = models.ForeignKey(User, on_delete = models.SET_NULL, null= True, blank =True, related_name='students')
    is_deleted = models.BooleanField(default=False)

    class Meta:
        db_table = 'STUDENT'
    def __str__(self):
        return self.name
