# Generated by Django 4.0.4 on 2022-05-01 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='is_done',
            field=models.BooleanField(default=False, verbose_name='Is done'),
        ),
    ]
