from django.db import models

class User(models.Model):
    id = models.AutoField(primary_key=True)
    dob = models.DateField()
    doa = models.DateField()

class Recording(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    audio_file = models.FileField(upload_to='recordings/')
    created_at = models.DateTimeField(auto_now_add=True)
    text_field = models.TextField(blank=True, null=True)
