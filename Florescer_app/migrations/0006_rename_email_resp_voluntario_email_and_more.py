# Generated by Django 4.2.5 on 2023-11-14 00:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Florescer_app', '0005_voluntario'),
    ]

    operations = [
        migrations.RenameField(
            model_name='voluntario',
            old_name='email_resp',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='voluntario',
            old_name='telefone_resp',
            new_name='telefone',
        ),
        migrations.RemoveField(
            model_name='voluntario',
            name='alergias',
        ),
        migrations.RemoveField(
            model_name='voluntario',
            name='nome_responsavel',
        ),
    ]
