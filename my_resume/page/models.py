from django.db import models

class Contact(models.Model):
    linkedin = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(max_length=50, blank=True, null=True)
    GitHub = models.CharField(max_length=50, blank=True, null=True)
    telephone = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.linkedin, self.email, self.GitHub, self.telephone

class Education(models.Model):
    course = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.course
    
class Skills(models.Model):
    skill = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.skill
    
class AboutMe(models.Model):
    about_me = models.TextField(max_length=1000, blank=True, null=True)

    def __str__(self):
        return self.about_me
    

