from django import forms
from dsrs_viz.models import D3_js, React_js, D3_react_js

class D3JSForm(forms.ModelForm):

    class Meta:
        model = D3_js
        fields = '__all__'

    # When the user fills up the form, I will further clean up the data and remove all the white spaces from it
    def clean_heading(self):
        return self.cleaned_data['heading'].strip()

    def clean_description(self):
        return self.cleaned_data['description'].strip()

    def clean_author(self):
        return self.cleaned_data['author'].strip()

    def clean_js_code(self):
        return self.cleaned_data['js_code'].strip()

    def clean_library_name(self):
        return self.cleaned_data['library_name'].strip()

    def clean_notes(self):
        return self.cleaned_data['notes'].strip()




class ReactJSForm(forms.ModelForm):

    class Meta:
        model = React_js
        fields = '__all__'

    # When the user fills up the form, I will further clean up the data and remove all the white spaces from it
    def clean_heading(self):
        return self.cleaned_data['heading'].strip()

    def clean_description(self):
        return self.cleaned_data['description'].strip()

    def clean_author(self):
        return self.cleaned_data['author'].strip()

    def clean_js_code(self):
        return self.cleaned_data['js_code'].strip()

    def clean_library_name(self):
        return self.cleaned_data['library_name'].strip()

    def clean_notes(self):
        return self.cleaned_data['notes'].strip()




class D3ReactJSForm(forms.ModelForm):

    class Meta:
        model = D3_react_js
        fields = '__all__'

    # When the user fills up the form, I will further clean up the data and remove all the white spaces from it
    def clean_heading(self):
        return self.cleaned_data['heading'].strip()

    def clean_description(self):
        return self.cleaned_data['description'].strip()

    def clean_author(self):
        return self.cleaned_data['author'].strip()

    def clean_js_code(self):
        return self.cleaned_data['js_code'].strip()

    def clean_library_name(self):
        return self.cleaned_data['library_name'].strip()

    def clean_notes(self):
        return self.cleaned_data['notes'].strip()