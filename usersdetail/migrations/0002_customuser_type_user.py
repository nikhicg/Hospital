# Generated by Django 3.2.4 on 2021-10-28 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usersdetail', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='type_user',
            field=models.CharField(choices=[('Doctor', 'Doctor'), ('Patients', 'Patients')], default='Doctor', max_length=10),
        ),
    ]