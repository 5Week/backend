# Generated by Django 4.2.3 on 2023-08-24 11:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_board_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='board',
            old_name='id',
            new_name='board_id',
        ),
    ]
