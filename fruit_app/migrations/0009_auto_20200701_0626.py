# Generated by Django 2.2.13 on 2020-07-01 06:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fruit_app', '0008_auto_20200701_0623'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commodity_data',
            name='country',
            field=models.ForeignKey(db_column='country', on_delete=django.db.models.deletion.CASCADE, related_name='country', to='fruit_app.Country'),
        ),
    ]
