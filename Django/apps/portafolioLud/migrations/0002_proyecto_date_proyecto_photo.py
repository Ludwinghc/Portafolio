# Generated by Django 4.2.5 on 2023-10-13 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portafolioLud', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='proyecto',
            name='date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='proyecto',
            name='photo',
            field=models.ImageField(null=True, upload_to='media/photoProjects'),
        ),
    ]