from django.db import models
from django.forms.models import model_to_dict
from django.core.serializers.json import DjangoJSONEncoder
import json
from django.core.validators import ValidationError
from django.db.models.constraints import CheckConstraint
from django.db.models import Q
import re

"""Models for the Django application fruit_app
These classes represent the database tables.
"""

class Country(models.Model):
    """Model for a Country.  Primary key is the 2-letter code.

    Country codes are described in Wikipedia:
        https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2
    The JSON string for this object is found at:
        https://gist.github.com/ssskip/5a94bfcd2835bf1dea52

    Note:
        Country is a Foreign Key for the CommodityData model, so the
        appropriate Country entry must be saved to the database before
        the CommodityData can be created.

    Attributes:
        country_code (str)
            2-letter country code is the Primary Key (must be unique)
        name (str)
            Full name of the country
        Meta (class)
            The Meta class contains Django model directives

            Attributes:
               app_label (str)
                   Name of the app (required by Sphinx package)
               constraints (list)

                   1)  the country_code must be 2 letters

                   2)  the name can only contain letters or spaces

    **Detailed Member Documentation**

    """

    name = 'Country'

    class Meta:
        """The metaclass contains database constraints"""

        app_label = 'fruit_app'

        constraints = [
            CheckConstraint(
                check=Q(country_code__regex=r'^[a-zA-Z]{2,2}'),
                name='country_2_letter_code'),
            CheckConstraint(check=Q(name__regex=r'^[a-zA-Z\s]+$'),
                            name='country_name'),
        ]

    country_code = models.CharField(
        primary_key=True,
        max_length=2,
        help_text='2-letter Country abbreviation',
        blank=False
    )
    name = models.CharField(
        max_length=64,
        blank=False
    )

    def clean(self, *args, **kwargs):
        """Validate country_code and convert to upper case
        """
        if re.match(r'^[a-zA-Z]{2}$', self.country_code) is None:
            raise ValidationError('country must be 2 letters')
        '''
        convert country to upper case
        '''
        self.country_code = self.country_code.upper()

    def save(self, *args, **kwargs):
        """Override default to call clean before super.save
        """
        self.full_clean()
        super(Country, self).save(*args, **kwargs)

    def __str__(self):
        """Return JSON string of model dictionary
        """
        return self.__repr__()

    def __repr__(self):
        """Represent the model as a JSON dictionary of its members.
        """
        model_dict = model_to_dict(self)
        return json.dumps(model_dict)


class CommodityData(models.Model):
    """Model for a CommodityData item.

    Attributes:
        country (ForeignKey)
            instance of Country model
        commodity (str)
            name of the commodity
        fixed_overhead (decimal 8.2)
            cost in U.S. dollars for a trade for this country and commodity
        variable_cost (decimal 8.2)
            cost in U.S. dollars for an additional ton
        Meta (class)
            The Meta class contains Django model directives

            Attributes:
               app_label (str)
                   Name of the app (required by Sphinx package)
               constraints (list)

                   1)  country and commodity combination must be  unique

                   2)  fixed_overhead must be >= 0

                   3)  variable_cost must be >= 0


    Note:
        * country and commodity combination must be unique
        * decimal values are limited to 99999.99
        * fixed_overhead must be >= 0
        * variable_cost must be >=0

    Example Item as JSON:
        "COUNTRY":"MX", "COMMODITY":"mango", "FIXED_OVERHEAD":"32.00",
        "VARIABLE_COST":"1.24"

    **Detailed Member Documentation**

    """

    class Meta:
        app_label = 'fruit_app'
        unique_together = (('country', 'commodity'),)
        constraints = [
            CheckConstraint(check=Q(fixed_overhead__gte=0),
                            name='fixed_overhead_not_negative'),
            CheckConstraint(check=Q(variable_cost__gte=0),
                            name='variable_cost_not_negative'),
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
        max_digits=8,
        decimal_places=2,
        default=0,
    )
    variable_cost = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        default=0,
    )

    def clean(self, *args, **kwargs):
        if self.fixed_overhead < 0:
            raise ValidationError('fixed_overhead must be >= 0')
        if self.variable_cost < 0:
            raise ValidationError('fixed_overhead must be >= 0')

    def save(self, *args, **kwargs):
        self.clean()
        super(CommodityData, self).save(*args, **kwargs)

    def __str__(self):
        """Return JSON string of model dictionary
        """
        return self.__repr__()

    def __repr__(self):
        """Represent the model as a JSON dictionary of its members.
        """
        model_dict = model_to_dict(self)
        return json.dumps(model_dict, cls=DjangoJSONEncoder)
