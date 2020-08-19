from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.http.response import HttpResponse
from django.template import loader
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, DeleteView, UpdateView

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
from .utils import PageLinksMixin


class D3JSList(LoginRequiredMixin, PermissionRequiredMixin, PageLinksMixin, ListView):
    paginate_by = 2
    model = D3_js
    permission_required = 'dsrs_viz.view_d3_js'





class D3JSDetail(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = 'dsrs_viz.view_d3_js'

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


class D3JSCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = D3JSForm
    model = D3_js
    permission_required = 'dsrs_viz.add_d3_js'


class D3JSUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    form_class = D3JSForm
    model = D3_js
    template_name = 'dsrs_viz/d3_js_form_update.html'
    permission_required = 'dsrs_viz.change_d3_js'


class D3JSDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = D3_js
    success_url = reverse_lazy('dsrs_viz_d3_js_list_urlpattern')
    permission_required = 'dsrs_viz.delete_d3_js'



#----------------------------------------------------------
# def react_js_list_view(request):
#     react_js_list = React_js.objects.all()
#     template = loader.get_template('dsrs_viz/react_js_list.html')
#     context = {'react_js_list': react_js_list}
#     output = template.render(context)
#     return HttpResponse(output)
#
#


class ReactJSList(LoginRequiredMixin, PermissionRequiredMixin, PageLinksMixin, ListView):
    paginate_by = 2
    model = React_js
    permission_required = 'dsrs_viz.view_react_js'



class ReactJSDetail(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = 'dsrs_viz.view_react_js'

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


class ReactJSCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = ReactJSForm
    model = React_js
    permission_required = 'dsrs_viz.add_react_js'

class ReactJSUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    form_class = ReactJSForm
    model = React_js
    template_name = 'dsrs_viz/react_js_form_update.html'
    permission_required = 'dsrs_viz.change_react_js'


class ReactJSDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = React_js
    success_url = reverse_lazy('dsrs_viz_react_js_list_urlpattern')
    permission_required = 'dsrs_viz.delete_react_js'

#----------------------------------------------------------

# def d3_react_js_list_view(request):
#     d3_react_js_list = D3_react_js.objects.all()
#     template = loader.get_template('dsrs_viz/d3_react_js_list.html')
#     context = {'d3_react_js_list': d3_react_js_list}
#     output = template.render(context)
#     return HttpResponse(output)




class D3ReactJSList(LoginRequiredMixin, PermissionRequiredMixin, PageLinksMixin, ListView):
    paginate_by = 2
    model = D3_react_js
    permission_required = 'dsrs_viz.view_d3_react_js'


class D3ReactJSDetail(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = 'dsrs_viz.view_d3_react_js'

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

class D3ReactJSCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = D3ReactJSForm
    model = D3_react_js
    permission_required = 'dsrs_viz.add_d3_react_js'

class D3ReactJSUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    form_class = D3ReactJSForm
    model = D3_react_js
    template_name = 'dsrs_viz/d3_react_js_form_update.html.html'
    permission_required = 'dsrs_viz.change_d3_react_js'

class D3ReactJSDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = D3_react_js
    success_url = reverse_lazy('dsrs_viz_d3_react_js_list_urlpattern')
    permission_required = 'dsrs_viz.delete_d3_react_js'


