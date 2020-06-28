# Generated by Django 2.2.13 on 2020-06-24 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fruit_app', '0002_auto_20200624_2135'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='commodity_data',
            constraint=models.CheckConstraint(check=models.Q(country__regex='^[a-zA-Z]{2,2}'), name='country_2_letters'),
        ),
        migrations.AddConstraint(
            model_name='commodity_data',
            constraint=models.CheckConstraint(check=models.Q(fixed_overhead__gte=0), name='fixed_overhead_not_negative'),
        ),
        migrations.AddConstraint(
            model_name='commodity_data',
            constraint=models.CheckConstraint(check=models.Q(variable_cost__gte=0), name='variable_cost_not_negative'),
        ),
    ]