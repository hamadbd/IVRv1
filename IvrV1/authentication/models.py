# models.py

from django.db import models
import bcrypt

class User(models.Model):
    id = models.AutoField(primary_key=True)
    dob = models.DateField()
    doa = models.DateField()
    password = models.CharField(max_length=128)
    
    def save(self, *args, **kwargs):
        self.password = bcrypt.hashpw(self.password.encode('utf-8'), bcrypt.gensalt())
        super().save(*args, **kwargs)

class Recording(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recording = models.FileField(upload_to='recordings/')
    created_at = models.DateTimeField(auto_now_add=True)
