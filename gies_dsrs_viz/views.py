from django.shortcuts import redirect

# This function will decide the landing page whenever
# a user open the website for the first time
def redirect_root_view(request):
    return redirect('dsrs_viz_d3_js_list_urlpattern')