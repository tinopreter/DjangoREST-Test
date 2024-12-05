from django.db import models

# Create your models here.
class Users(models.Model):
    username = models.CharField(max_length=30, blank=False, unique=True)
    email = models.EmailField(max_length=50, blank=False, unique=True)
    fullname = models.CharField(max_length=80, blank=True)
    isAdmin = models.BooleanField(default=False)
    createdAt = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.username

    class Meta:
        ordering = ['id']
        