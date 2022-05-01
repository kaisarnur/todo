# Generated by Django 4.0.4 on 2022-05-01 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('description', models.TextField(max_length=3000, verbose_name='Description')),
                ('execution_time', models.DateTimeField(verbose_name='Execution Time')),
                ('is_done', models.BooleanField(verbose_name='Is done')),
            ],
        ),
    ]