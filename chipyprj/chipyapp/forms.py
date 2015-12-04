from django import forms
from models import Module

class DatatableForm(forms.Form):
    sorting = forms.CharField(required = False)
    filter_lob = forms.CharField(required = False)
    filter_year= forms.IntegerField(required = False, max_value=2020, min_value=2010)
    filter_quarter= forms.IntegerField(required = False, max_value=4, min_value=1)
    num_line = forms.IntegerField()

    def clean_sorting(self):
        data = self.cleaned_data['sorting']
        valid_list = ['year', 'quarter','penetration','-year','-quarter','-penetration']
        if not data:
           return '-penetration'
        elif data not in valid_list:
           raise forms.ValidationError("Bad sort field!")
        return data   
  
    def clean_filter_lob(self):
        data = self.cleaned_data['filter_lob']
        valid_list = ['Video', 'HSD','CDV','XHS','',None]
        if data not in valid_list:
           raise forms.ValidationError("Bad LOB filter field!")
        return data


class ChartFilterForm(forms.Form):
    filter_module = forms.ModelMultipleChoiceField(
        queryset=Module.objects.all(),
        widget=forms.SelectMultiple(attrs={"class": "form-control"}))
