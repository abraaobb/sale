# Generated by Django 4.0.4 on 2022-05-20 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='gender',
            field=models.CharField(default='M', max_length=1),
        ),
    ]
