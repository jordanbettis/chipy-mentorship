from django.shortcuts import render
from .models import Module, Area, Complex, LOB, Penetration, ActiveUnit
from .forms import DatatableForm, ChartFilterForm
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
    form_filters = {}
    if request.method == 'POST':
        form = ChartFilterForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            module_selected = cd['filter_module']
            if module_selected.exists():
                form_filters['module__in'] = module_selected

    else:
        form = ChartFilterForm()


    pen_data = []
    quarters = set()
    for lob in LOB.objects.all():

        lob_data = [lob.lob]
        lob_result = Penetration.objects.filter(lob=lob)
        if form_filters:
            lob_result = lob_result.filter(**form_filters)
        lob_result.values('quarter').annotate(avg_pen=Avg('penetration'))
        for r in lob_result:
            lob_data.append(r['avg_pen'])
            quarters.add(r['quarter'])
        pen_data.append(lob_data)
    pen_data.append(['x']+list(quarters))
    chart_data = json.dumps(pen_data, indent=4)
    return render(request, 'chipyapp/chart.html', locals())


    
