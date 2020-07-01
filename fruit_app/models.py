from django.db import models
from django.forms.models import model_to_dict
from django.core.serializers.json import DjangoJSONEncoder
import json
from django.core.validators import ValidationError
from django.db.models.constraints import CheckConstraint
from django.db.models import Q
import re

class Country(models.Model):

    class Meta:
        constraints = [
            CheckConstraint(check=Q(country_code__regex=r'^[a-zA-Z]{2,2}'), name='country_2_letter_code'),
            CheckConstraint(check=Q(name__regex=r'^[a-zA-Z\s]+$'), name='country_name'),
        ]

    country_code = models.CharField(
        primary_key=True,
        max_length = 2,
        help_text = '2-letter Country abbreviation',
        blank=False
    )
    name = models.CharField(
        max_length = 64,
        blank=False
    )

    def clean(self, *args, **kwargs):
        if re.match(r'^[a-zA-Z]{2,2}$', self.country_code) is None:
            raise ValidationError('country must be 2 letters')
        '''
        convert country to upper case
        '''
        self.country_code = self.country_code.upper()

    def save(self, *args, **kwargs):
        self.full_clean()
        super(Country, self).save(*args, **kwargs)

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        model_dict = model_to_dict(self)
        return json.dumps(model_dict)


class Commodity_Data(models.Model):
    """
    Commodity_Data Model
    Defines the attributes of a commodity

    example:
    "COUNTRY":"MX", "COMMODITY":"mango", "FIXED_OVERHEAD":"32.00", "VARIABLE_COST":"1.24"
    """
    class Meta:
        unique_together = (('country', 'commodity'),)
        constraints = [
            # CheckConstraint(check=Q(country__regex=r'^[a-zA-Z]{2,2}'), name='country_2_letter_code'),
            CheckConstraint(check=Q(fixed_overhead__gte=0), name='fixed_overhead_not_negative'),
            CheckConstraint(check=Q(variable_cost__gte=0), name='variable_cost_not_negative'),
        ]

    country = models.ForeignKey(
        Country,
        db_column='country',
        related_name='country',
        on_delete=models.CASCADE
        )

    commodity = models.CharField(
        max_length=255,
        blank=False
        )
    fixed_overhead = models.DecimalField(
        max_digits = 8,
        decimal_places = 2,
        default = 0,
        )
    variable_cost = models.DecimalField(
        max_digits = 8,
        decimal_places = 2,
        default = 0,
        )

    def clean(self, *args, **kwargs):
        if re.match(r'^[a-zA-Z]{2,2}$', self.country) is None:
            raise ValidationError('country must be 2 letters')
        '''
        convert country to upper case
        '''
        self.country = self.country.upper()
        if (self.fixed_overhead < 0):
            raise ValidationError('fixed_overhead must be >= 0')
        if (self.variable_cost < 0):
            raise ValidationError('fixed_overhead must be >= 0')
        # super(BaseModel, self).clean(*args, **kwargs)

    def save(self, *args, **kwargs):
        self.full_clean()
        super(Commodity_Data, self).save(*args, **kwargs)

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        model_dict = model_to_dict(self)
        return json.dumps(model_dict, cls=DjangoJSONEncoder)



