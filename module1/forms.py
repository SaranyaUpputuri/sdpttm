from django import forms

class Integerdateform(forms.Form):
    integer_value=forms.IntegerField()
    date_value=forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))