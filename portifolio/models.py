from django.db import models

class ProjectModel(models.Model):
    imagehero = models.ImageField(upload_to="project", default="project.png")
    title = models.CharField(max_length=24)
    desc = models.CharField(max_length=56)

    about = models.TextField()

    profile = models.ImageField(upload_to='profile', default="profile.png")
    feedback =models.TextField(default="")
    name = models.CharField(max_length=24)

    def __str__(self):
        return self.title
    
