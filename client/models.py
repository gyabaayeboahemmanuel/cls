from django.db import models

# Create your models here.
class Client (models.Model):
    FirstName = models.CharField(max_length=255, verbose_name="First Name")
    LastName = models.CharField(max_length=255, verbose_name="Last Name")
    MiddleName = models.CharField(max_length=255, verbose_name="Middle Name",default=".", blank=True, null=True)
    PhoneNumber = models.CharField(max_length=255, verbose_name="Phone Number")
    email = models.EmailField(max_length=255,null=True, blank=True, verbose_name="Email")
    dateofbirth = models.DateTimeField( verbose_name="Date of Birth")
    GhanaCard = models.CharField(max_length=255, verbose_name="Ghana Card Number")
    profile_picture = models.ImageField(upload_to = "profile/", null=True, blank=True)
    dateSignedUp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.FirstName + " " + self.LastName + " |Ghana Card: " + self.GhanaCard
