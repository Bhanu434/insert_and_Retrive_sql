# Generated by Django 4.2.6 on 2023-12-15 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='emp',
            name='id',
        ),
        migrations.AlterField(
            model_name='emp',
            name='Empno',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
