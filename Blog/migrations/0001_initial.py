# Generated by Django 3.2.4 on 2021-11-01 12:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('Technology', 'Technology'), ('Entairnment', 'Entairnment')], max_length=20)),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('summary', models.CharField(max_length=500)),
                ('image', models.ImageField(upload_to='profile_pics')),
                ('content', models.TextField()),
                ('draft', models.BooleanField(default=False)),
                ('about_you', models.TextField(blank=True)),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]