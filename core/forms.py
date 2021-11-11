from django.forms import ModelForm
from django import forms
from core.models import ShopInfo, Customer


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name']


class MyDateInput(forms.DateInput):
    input_type = 'date'
    format = '%Y-%m-%d'


class ShopInfoForm(ModelForm):
    # customer = forms.ModelMultipleChoiceField(
    #     queryset=Customer.objects.all(),
    #     widget=forms.CheckboxSelectMultiple
    # )
    purchase_date = forms.DateField(
        label='дата покупки', required=True,
        widget=MyDateInput({
            'class': 'form-control'
        }))

    class Meta:
        model = ShopInfo
        fields = '__all__'
