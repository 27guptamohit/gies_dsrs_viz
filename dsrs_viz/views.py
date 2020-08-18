from django.shortcuts import render
from django.http.response import HttpResponse
from django.template import loader

from .models import (
    D3_js,)

def d3_js_list_view(request):
    d3_js_list = D3_js.objects.all()
    template = loader.get_template('dsrs_viz/d3_js_list.html')
    context = {'d3_js_list': d3_js_list}
    output = template.render(context)
    return HttpResponse(output)




