# Generated by Django 2.2.13 on 2020-07-01 00:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fruit_app', '0004_auto_20200625_0100'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(help_text='2-letter Country abbreviation', max_length=2)),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.RemoveConstraint(
            model_name='commodity_data',
            name='country_2_letters',
        ),
        migrations.AddConstraint(
            model_name='commodity_data',
            constraint=models.CheckConstraint(check=models.Q(country__regex='^[a-zA-Z]{2,2}'), name='country_2_letter_code'),
        ),
        migrations.AddConstraint(
            model_name='country',
            constraint=models.CheckConstraint(check=models.Q(country__regex='^[a-zA-Z]{2,2}'), name='country_2_letter_code'),
        ),
        migrations.AddConstraint(
            model_name='country',
            constraint=models.CheckConstraint(check=models.Q(name__regex='^[a-zA-Z\\s]+$'), name='country_name'),
        ),
    ]
