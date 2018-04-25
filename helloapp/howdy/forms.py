from django import forms


class NameForm(forms.Form):
    city_input = forms.CharField(label='City', max_length=100)
