from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

import csv

class NameForm(forms.Form):

    city_input = forms.CharField(label='City', help_text="Enter a city name.", max_length=100, required=True)

    def clean_city_input(self):
        data = self.cleaned_data['city_input']
        name = data.lower().split(',')[0] # lower case and remove any reference to state
        # check if the city is in the csv file
        valid_city = False
        with open("dummy_csv.csv", "rb") as f:
            csvreader = csv.reader(f, delimiter=",")
            for row in csvreader:
                if name in row[0]:
                    valid_city = True
                    break
        if not valid_city:
            raise ValidationError(_('Invalid city name'))
        return name
