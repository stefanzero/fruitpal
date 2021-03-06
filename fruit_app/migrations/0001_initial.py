# Generated by Django 2.2.13 on 2020-06-24 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Commodity_Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(help_text='2-letter Country abbreviation', max_length=2)),
                ('commodity', models.CharField(max_length=255)),
                ('fixed_overhead', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('variable_cost', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
            ],
        ),
    ]
