from django import forms

class NewCustomer(forms.Form):
    full_name = forms.CharField(max_length=100)
    address1 = forms.CharField(max_length=100)
    address2 = forms.CharField(max_length=100)
    state = forms.CharField(max_length=100)
    city = forms.CharField(max_length=100)
    country= forms.CharField(max_length=100)