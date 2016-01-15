from django import forms
from models import Module, Area

class DatatableForm(forms.Form):
    sorting = forms.CharField(required = False)
    filter_lob = forms.CharField(required = False)
    filter_year = forms.IntegerField(required = False, max_value=2020, min_value=2010)
    filter_quarter = forms.IntegerField(required = False, max_value=4, min_value=1)
#    filter_module = forms.IntegerField()
#    filter_type = forms.CharField(required = False)
#    filter_team = forms.CharField(required = False)
#    filter_area = forms.CharField(required = False)
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
        valid_list = ['TV', 'Internet','Voice','Home','',None]
        if data not in valid_list:
           raise forms.ValidationError("Bad LOB filter field!")
        return data

    def clean_filter_type(self):
        data = self.cleaned_data['filter_type']
        valid_list = ['Bulk','Retail','',None]
        if data not in valid_list:
           raise forms.ValidationError("Bad Service Type filter field!")
        return data

    def clean_filter_team(self):
        data = self.cleaned_data['filter_team']
        valid_list = ['Team 1','Team 2','',None]
        if data not in valid_list:
           raise forms.ValidationError("Bad Team filter field!")
        return data

    def clean_filter_area(self):
        data = self.cleaned_data['filter_area']
        valid_list = ['City','North','West','South','',None]
        if data not in valid_list:
           raise forms.ValidationError("Bad Area filter field!")
        return data

class ChartFilterForm(forms.Form):
    filter_module = forms.ModelMultipleChoiceField(
        label = "Please Select Module(s)",
        queryset=Module.objects.all(),
        required=False,
        widget=forms.SelectMultiple(attrs={"class": "form-control"}))
    filter_area = forms.ModelMultipleChoiceField(
        label = "Please Select Area(s)",
        queryset=Area.objects.all(),
        required=False,
        widget=forms.SelectMultiple(attrs={"class": "form-control"}))
