from django.shortcuts import render
from .models import Module, Area, Complex, LOB, Penetration, ActiveUnit
from .forms import DatatableForm, ChartFilterForm
from django.db.models import Avg 
import json
from urllib import urlencode
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def dataform(request):
    if request.method == 'POST':
        form = DatatableForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            query = {'page': 1}
            query.update(cd)
            query = {k:v for k,v in query.items() if v is not None}
            rurl = reverse('datatable')
            return HttpResponseRedirect("{}?{}".format(rurl,urlencode(query)))
    else:
        form = DatatableForm(initial={"num_line":50, "quater": "", "year":"" })
    return render(request, 'chipyapp/dataform.html', locals())

def datatable(request):
    cd = request.GET
    sorting = cd['sorting']
    pen_data = Penetration.objects.select_related('complex_code')
    if cd.get('filter_lob'):
        pen_data = pen_data.filter(lob__lob = cd['filter_lob'])
    if cd.get('filter_year'):
        pen_data = pen_data.filter(year = cd['filter_year'])
    if cd.get('filter_quarter'):
        pen_data = pen_data.filter(quarter = cd['filter_quarter'])
#    if cd.get('filter_module'):
#        pen_data = pen_data.filter(complex_code__module = cd['filter_module'])
#    if cd.get('filter_type'):
#        pen_data = pen_data.filter(complex_code__service_status = cd['filter_type'])
#    if cd.get('filter_team'):
#        pen_data = pen_data.filter(complex_code__team = cd['filter_team'])
#    if cd.get('filter_area'):
#        pen_data = pen_data.filter(complex_code__area = cd['filter_area'])
    pen_data = pen_data.order_by(sorting)
    paginator = Paginator(pen_data, cd.get("num_line", 50))
    try:
        page_data = paginator.page(cd.get("page",1))
    except PageNotAnInteger:
        page_data = paginator.page(1)
    except EmptyPage:
        page_data = paginator.page(paginator.num_pages)
    if page_data.has_previous():
        previouscd = cd.copy()
        previouscd['page'] = page_data.previous_page_number()
        previousqs = urlencode(previouscd)
    if page_data.has_next():
        nextcd = cd.copy()
        nextcd['page'] = page_data.next_page_number()
        nextqs = urlencode(nextcd)
    firstcd = cd.copy()
    firstcd['page'] = paginator.page(1)
    firstqs = urlencode(firstcd)
    lastcd = cd.copy()
    lastcd['page'] = paginator.num_pages
    lastqs = urlencode(lastcd)

    return render(request, 'chipyapp/datatable.html', locals())

def chart(request):
    form_filters = {}
    if request.method == 'POST':
        form = ChartFilterForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            module_selected = cd['filter_module']
            area_selected = cd['filter_area']
            if module_selected.exists():
                form_filters['complex_code__module__in'] = module_selected
            if area_selected.exists():
                form_filters['complex_code__area__in'] = area_selected


    else:
        form = ChartFilterForm()

    pen_data = []
    quarters = set()
    for lob in LOB.objects.all():

        lob_data = [lob.lob]
        lob_result = Penetration.objects.filter(lob=lob)
        if form_filters:
            lob_result = lob_result.filter(**form_filters)
        lob_result = lob_result.values('quarter').annotate(avg_pen=Avg('penetration')).order_by('quarter')
        for r in lob_result:
            lob_data.append(r['avg_pen'])
            quarters.add(r['quarter'])
        pen_data.append(lob_data)
    pen_data.append(['x']+list(quarters))
    chart_data = json.dumps(pen_data, indent=4)
    return render(request, 'chipyapp/chart.html', locals())
