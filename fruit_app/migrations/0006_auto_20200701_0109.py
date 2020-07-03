# Generated by Django 2.2.13 on 2020-07-01 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fruit_app', '0005_auto_20200701_0026'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='country',
            name='id',
        ),
        migrations.AlterField(
            model_name='country',
            name='country',
            field=models.CharField(help_text='2-letter Country abbreviation', max_length=2, primary_key=True, serialize=False),
        ),
    ]
