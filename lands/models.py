from django.db import models

# Create your models here.
class Land (models.Model):
    plot= models.CharField(max_length=255)
    block= models.CharField(max_length=255)
    sector= models.CharField(max_length=255)
    location= models.CharField(max_length=255)

    def __str__(self):
        return self.plot + " " + self.block + " " +self.sector+ " " +self.location+ " " 