# Generated by Django 3.2 on 2021-06-25 01:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MovieData', '0003_movieinfo_genre'),
    ]

    operations = [
        migrations.AddField(
            model_name='movieinfo',
            name='image',
            field=models.ImageField(default='media/images/none.jpg', upload_to='media'),
        ),
    ]
