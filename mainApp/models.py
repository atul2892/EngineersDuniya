from django.db import models
from ckeditor.fields import RichTextField

class CallBackDetail(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return str(self.id)+" "+self.name
    
class ContactDetail(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    subject = models.CharField(max_length=1000)
    message = models.TextField()

    def __str__(self):
        return str(self.id)+" "+self.name

class TeamMember(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to="uploads")
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    about = models.TextField()

    def __str__(self):
        return str(self.id)+" "+self.name
    
class BlogPost(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to="uploads")
    date = models.DateField(auto_now=True)
    title = models.CharField(max_length=1000)
    content = RichTextField()
    summery = models.TextField(default="",blank=True)

    def __str__(self):
        return str(self.id)+" "+self.title
    
class BlogComment(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    date = models.DateField(auto_now=True)
    message = models.TextField()
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name="BlogComment")
    
    def __str__(self):
        return str(self.id)+" "+self.username
    
    
class Subscribtion(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField()

    def __str__(self):
        return str(self.id)+" "+self.email
