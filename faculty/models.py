from django.db import models

class Faculty(models.Model):
    name = models.CharField(max_length=100)
    academic_rank = models.CharField(max_length=50)
    department = models.CharField(max_length=100)
    education = models.TextField()
    research_interests = models.TextField()
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    profile_image = models.ImageField(upload_to='profiles/', blank=True, null=True)
    resume_file = models.FileField(upload_to='resumes/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name