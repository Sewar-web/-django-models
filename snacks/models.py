from django.db import models

# Create your models here.

class snacks(models.Model):
    name=models.CharField(max_length=64)
    desc=models.TextField()
    purchaser=models.ForeignKey('auth.User', on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.name
