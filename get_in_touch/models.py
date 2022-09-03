from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=150)
    surname = models.CharField(max_length=255, default="Some String")
    #address = models.CharField(max_length=300)
    #city = models.CharField(max_length=150)
    # state_of_province = models.CharField(max_length=150)
    phone = models.CharField(max_length=15, default='')
    mobile = models.CharField(max_length=15, default='')
    email = models.EmailField(default='')
    subject = models.TextField(max_length=150)
    massage = models.TextField(max_length=150)
    company = models.CharField(max_length=255, default="Some String")
    role = models.CharField(max_length=50, null=True)
    

    def __str__(self):
        return self.name

