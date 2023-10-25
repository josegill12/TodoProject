from django.db import models

class Todo(models.Model):
    subject = models.CharField(max_length=100)
    details = models.CharField(max_length=100)


class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    
class Completed(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)