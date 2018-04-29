from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

import os
import csv

class NameForm(forms.Form):

    city_input = forms.CharField(label='City', help_text="Enter a city name.", max_length=100, required=True)

    def clean_city_input(self):
        data = self.cleaned_data['city_input']
        name = data.split(',')[0] # lower case and remove any reference to state
        # check if the city is in the csv file
        valid_city = False
        fname = os.path.join(os.path.dirname(__file__), 'dummy_csv.csv')
        with open(fname, "r") as f:
            csvreader = csv.reader(f, delimiter=",")
            for row in csvreader:
                if name.lower() in row[0].lower():
                    valid_city = True
                    break
        if not valid_city:
            raise ValidationError(_('Invalid city name'))
        return name
