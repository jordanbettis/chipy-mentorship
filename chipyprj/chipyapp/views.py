from django.shortcuts import render
from .models import Module, Area, Complex, LOB, Penetration, ActiveUnit
from .forms import DatatableForm
from django.db.models import Avg 
import json

def datatable(request):
    if request.method == 'POST':
         form = DatatableForm(request.POST)
         if form.is_valid():
            cd = form.cleaned_data
            sorting = cd['sorting']
            pen_data = Penetration.objects.select_related('complex_code')
            if cd['filter_lob']:
                pen_data = pen_data.filter(lob__lob = cd['filter_lob'])   
            if cd['filter_year']:
                pen_data = pen_data.filter(year = cd['filter_year'])  
            if cd['filter_quarter']:
                pen_data = pen_data.filter(quarter = cd['filter_quarter'])
            pen_data = pen_data.order_by(sorting)
            pen_data = pen_data[:cd['num_line']]
    else:
        form = DatatableForm(initial={"num_line":50})
    return render(request, 'chipyapp/datatable.html', locals())

def chart(request):
    pen_data = LOB.objects.annotate(avg_pen=Avg('penetration__penetration'))
    chart_data = json.dumps([{'LOB': i.lob,'Avg_Pen': i.avg_pen} for i in pen_data])
    return render(request, 'chipyapp/chart.html', locals())
    
