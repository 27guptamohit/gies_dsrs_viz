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
from dsrs_viz.views import (D3JSList, ReactJSList, D3ReactJSList,
                            D3JSDetail, ReactJSDetail, D3ReactJSDetail,
                            D3JSCreate, ReactJSCreate, D3ReactJSCreate)


# The url pattern names will be helpful while pointing back from href attribute
urlpatterns = [
    path('d3_js/', D3JSList.as_view(),
         name='dsrs_viz_d3_js_list_urlpattern'),
    path('d3_js/<int:pk>/',
         D3JSDetail.as_view(),
         name='dsrs_viz_d3_js_detail_urlpattern'),
    path('d3_js/create/', D3JSCreate.as_view(),
         name='dsrs_viz_d3_js_create_urlpattern'),




    path('react_js/', ReactJSList.as_view(),
         name='dsrs_viz_react_js_list_urlpattern'),
    path('react_js/<int:pk>/', ReactJSDetail.as_view(),
         name='dsrs_viz_react_js_detail_urlpattern'),
    path('react_js/create/', ReactJSCreate.as_view(),
         name='dsrs_viz_react_js_create_urlpattern'),




    path('d3_react_js/', D3ReactJSList.as_view(),
         name='dsrs_viz_d3_react_js_list_urlpattern'),
    path('d3_react_js/<int:pk>/', D3ReactJSDetail.as_view(),
         name='dsrs_viz_d3_react_js_detail_urlpattern'),
    path('d3_react_js/create/', D3ReactJSCreate.as_view(),
         name='dsrs_viz_d3_react_js_create_urlpattern'),
]
