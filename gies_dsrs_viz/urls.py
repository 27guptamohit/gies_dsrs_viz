"""gies_dsrs_viz URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from dsrs_viz.views import  (
    d3_js_list_view,
react_js_list_view,
d3_react_js_list_view,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('d3_js/', d3_js_list_view),
    path('react_js/', react_js_list_view),
    path('d3_react_js/', d3_react_js_list_view),

]
