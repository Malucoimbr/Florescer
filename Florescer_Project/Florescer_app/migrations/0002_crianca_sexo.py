# Generated by Django 4.2.5 on 2023-10-16 19:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Florescer_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='crianca',
            name='sexo',
            field=models.CharField(default=django.utils.timezone.now, max_length=5),
            preserve_default=False,
        ),
    ]