from django.contrib import admin
from .models import D3_js, React_js, D3_react_js




admin.site.register(D3_js)
admin.site.register(React_js)
admin.site.register(D3_react_js)
admin.site.site_header = 'DSRS Visualization Portal'
admin.site.site_title = 'DSRS Visualization Portal'