from django.shortcuts import render
from django.http.response import HttpResponse
from django.template import loader
from django.views import View

from .models import (
    D3_js,
    React_js,
    D3_react_js,
)

# Function based view
# def d3_js_list_view(request):
#     d3_js_list = D3_js.objects.all()
#     template = loader.get_template('dsrs_viz/d3_js_list.html')
#     context = {'d3_js_list': d3_js_list}
#     output = template.render(context)
#     return HttpResponse(output)


# def react_js_list_view(request):
#     react_js_list = React_js.objects.all()
#     template = loader.get_template('dsrs_viz/react_js_list.html')
#     context = {'react_js_list': react_js_list}
#     output = template.render(context)
#     return HttpResponse(output)
#
#
# def d3_react_js_list_view(request):
#     d3_react_js_list = D3_react_js.objects.all()
#     template = loader.get_template('dsrs_viz/d3_react_js_list.html')
#     context = {'d3_react_js_list': d3_react_js_list}
#     output = template.render(context)
#     return HttpResponse(output)


# Class based view
class D3JSList(View):

    def get(self, request):
        return render(
            request,
            'dsrs_viz/d3_js_list.html',
            {'d3_js_list': D3_js.objects.all()}
        )


class ReactJSList(View):

    def get(self, request):
        return render(
            request,
            'dsrs_viz/react_js_list.html',
            {'react_js_list': React_js.objects.all()}
        )


class D3ReactJSList(View):

    def get(self, request):
        return render(
            request,
            'dsrs_viz/d3_react_js_list.html',
            {'d3_react_js_list': D3_react_js.objects.all()}
        )