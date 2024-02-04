from django.db import models

# Create your models here.
class UserProfile(models.Model):
    resume= models.TextField()
    job_post=models.TextField()
    customized_resume=models.TextField(blank=True, null=True)

    