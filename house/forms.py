from django import forms
from django_countries.fields import CountryField
from . import models

class SearchForm(forms.Form):
    country = CountryField(blank=True).formfield()
    city = forms.CharField(initial="", required=False)
    house_type = forms.ModelChoiceField(
        empty_label="Any kind", queryset=models.HouseType.objects.all(),
        required=False
    )
    price = forms.IntegerField(required=False)
    guests = forms.IntegerField(required=False)
    bedrooms = forms.IntegerField(required=False)
    beds = forms.IntegerField(required=False)
    baths = forms.IntegerField(required=False)

    amenities = forms.ModelMultipleChoiceField(
        queryset=models.Amenity.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )
    facilities = forms.ModelMultipleChoiceField(
        queryset=models.Facility.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )
