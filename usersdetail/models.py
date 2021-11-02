from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from PIL import Image


class CustomUser(AbstractUser):
    user_type = (('Doctor', 'Doctor'),
                 ('Patients', 'Patients')
                 )
    type_user = models.CharField(
        choices=user_type, default='Doctor', max_length=10)
    profile_picture = models.ImageField(
        upload_to='profile_pics', null=True, blank=True)
    email_id = models.EmailField(_('email'), unique=True)
    address_line1 = models.TextField()
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    pincode = models.CharField(max_length=100)

    def __str__(self):
        return self.username

    """def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.profile_picture.path)

        if img.height > 200 or img.width > 200:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.profile_picture.path)"""
