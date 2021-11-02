from usersdetail.models import CustomUser
from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.utils.text import slugify
from PIL import Image


class Post(models.Model):
    field_type = models.TextChoices(
        'field_type', 'Mental_Health, Heart_Disease, Covid19, Immunization')
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    category = models.CharField(choices=field_type.choices, max_length=20)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    summary = models.CharField(max_length=500)
    image = models.ImageField(upload_to='profile_pics')
    content = models.TextField()
    set_as_draft = models.BooleanField(default=False)
    date_posted = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-date_posted']

    def __str__(self):
        return self.slug

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)
        q = img.resize((600, 350))
        q.save(self.image.path)
