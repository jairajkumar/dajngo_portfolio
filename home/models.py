from django.db import models

# Create your models here.

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class skill(models.Model):
    name = models.TextField(max_length=50)
    status = models.IntegerField(choices=STATUS, default=0)


    def __str__(self):
        return (self.name)


class Contact(models.Model):
    sno = models.AutoField(primary_key = True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    message = models.TextField(max_length=500)
    timestamp = models.DateTimeField(auto_now_add= True,blank = True)

    def __str__(self):
        return (self.name)