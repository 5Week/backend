# Generated by Django 4.2.3 on 2023-08-24 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_board_options_alter_board_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
