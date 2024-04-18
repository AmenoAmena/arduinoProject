from django.db import models

# Create your models here.
class sensorImage(models.Model):
    name = models.CharField(max_length=16,default='Sensor')
    image = models.ImageField(upload_to='media/')

    def __str__(self):
        return f"Image: {self.name}"

class item(models.Model):
    name = models.CharField(max_length=40)
    number = models.PositiveIntegerField()
    image = models.ForeignKey(sensorImage,on_delete=models.CASCADE)
    