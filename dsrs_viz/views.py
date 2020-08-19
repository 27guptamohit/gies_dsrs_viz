from django.shortcuts import render, get_object_or_404
from django.http.response import HttpResponse
from django.template import loader
from django.views import View

from .forms import D3JSForm, ReactJSForm, D3ReactJSForm
from .models import (
    D3_js,
    React_js,
    D3_react_js,
)




#----------------------------------------------------------
# Function based view
# def d3_js_list_view(request):
#     d3_js_list = D3_js.objects.all()
#     template = loader.get_template('dsrs_viz/d3_js_list.html')
#     context = {'d3_js_list': d3_js_list}
#     output = template.render(context)
#     return HttpResponse(output)




# Class based view
from .utils import ObjectCreateMixin


class D3JSList(View):

    def get(self, request):
        return render(
            request,
            'dsrs_viz/d3_js_list.html',
            {'d3_js_list': D3_js.objects.all()}
        )


class D3JSDetail(View):

    def get(self, request, pk):
        d3_js = get_object_or_404(
            D3_js,
            pk=pk
        )

        return render(
            request,
            'dsrs_viz/d3_js_detail.html',
            {'d3_js':d3_js}
        )


class D3JSCreate(ObjectCreateMixin, View):
    form_class = D3JSForm
    template_name = 'dsrs_viz/d3_js_form.html'




#----------------------------------------------------------
# def react_js_list_view(request):
#     react_js_list = React_js.objects.all()
#     template = loader.get_template('dsrs_viz/react_js_list.html')
#     context = {'react_js_list': react_js_list}
#     output = template.render(context)
#     return HttpResponse(output)
#
#


class ReactJSList(View):

    def get(self, request):
        return render(
            request,
            'dsrs_viz/react_js_list.html',
            {'react_js_list': React_js.objects.all()}
        )


class ReactJSDetail(View):

    def get(self, request, pk):
        react_js = get_object_or_404(
            React_js,
            pk=pk
        )

        return render(
            request,
            'dsrs_viz/react_js_detail.html',
            {'react_js': react_js}
        )


class ReactJSCreate(ObjectCreateMixin, View):
    form_class = ReactJSForm
    template_name = 'dsrs_viz/react_js_form.html'

#----------------------------------------------------------

# def d3_react_js_list_view(request):
#     d3_react_js_list = D3_react_js.objects.all()
#     template = loader.get_template('dsrs_viz/d3_react_js_list.html')
#     context = {'d3_react_js_list': d3_react_js_list}
#     output = template.render(context)
#     return HttpResponse(output)




class D3ReactJSList(View):

    def get(self, request):
        return render(
            request,
            'dsrs_viz/d3_react_js_list.html',
            {'d3_react_js_list': D3_react_js.objects.all()}
        )


class D3ReactJSDetail(View):

    def get(self, request, pk):
        d3_react_js = get_object_or_404(
            D3_react_js,
            pk=pk
        )

        return render(
            request,
            'dsrs_viz/d3_react_js_detail.html',
            {'d3_react_js': d3_react_js}
        )

class D3ReactJSCreate(ObjectCreateMixin, View):
    form_class = D3ReactJSForm
    template_name = 'dsrs_viz/d3_react_js_form.html'