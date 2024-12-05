from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    class Types(models.TextChoices):
        TEACHER = "TEACHER", "Teacher"
        STUDENT = "STUDENT", "Student"
        ADMINISTRATION = "ADMINISTRATION", "Administration"
    user_type = models.CharField(max_length=20, choices=Types.choices, default=Types.STUDENT)

    email = models.CharField(max_length=255)
    username = models.CharField(max_length=255,unique=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        db_table = 'users'
        
    def save(self, *args, **kwargs):
        if self.pk is None:  
            self.set_password(self.password)
        super().save(*args, **kwargs)