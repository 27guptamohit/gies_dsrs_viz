from django.db import models
from django.urls import reverse

class D3_js(models.Model):
    figure_no = models.AutoField(primary_key=True)
    library_name = models.CharField(unique=False, max_length=255)
    heading = models.TextField(unique=True)
    description = models.TextField(unique=False)
    js_code = models.TextField(unique=False)
    notes = models.TextField(unique=False, default='Please enter some notes')
    author = models.CharField(unique=False, max_length=255, default='Mohit Gupta')

    def __str__(self):
        return f'{self.figure_no}  -  {self.library_name}  -  {self.heading})'

    def get_absolute_url(self):
        # Reverse will take you back and forth to the visualization detail
        # that you will click
        return reverse('dsrs_viz_d3_js_detail_urlpattern',
                       kwargs={'pk':self.pk}
                       )

    def get_update_url(self):
        return reverse('dsrs_viz_d3_js_update_urlpattern',
                       kwargs={'pk':self.pk})

    class Meta:
        ordering = ['figure_no', 'library_name', 'heading']
        unique_together = ['figure_no', 'library_name', 'heading']






class React_js(models.Model):
    figure_no = models.AutoField(primary_key=True)
    library_name = models.CharField(unique=False, max_length=255)
    heading = models.TextField(unique=True)
    description = models.TextField(unique=False)
    js_code = models.TextField(unique=False)
    notes = models.TextField(unique=False, default='Please enter some notes')
    author = models.CharField(unique=False, max_length=255, default='Mohit Gupta')

    def __str__(self):
        return f'{self.figure_no}  -  {self.library_name}  -  {self.heading})'


    def get_absolute_url(self):
        # Reverse will take you back and forth to the visualization detail
        # that you will click
        return reverse('dsrs_viz_react_js_detail_urlpattern',
                       kwargs={'pk':self.pk}
                       )

    def get_update_url(self):
        return reverse('dsrs_viz_react_js_update_urlpattern',
                       kwargs={'pk':self.pk})

    class Meta:
        ordering = ['figure_no', 'library_name', 'heading']
        unique_together = ['figure_no', 'library_name', 'heading']





class D3_react_js(models.Model):
    figure_no = models.AutoField(primary_key=True)
    library_name = models.CharField(unique=False, max_length=255)
    heading = models.TextField(unique=True)
    description = models.TextField(unique=False)
    js_code = models.TextField(unique=False)
    notes = models.TextField(unique=False, default='Please enter some notes')
    author = models.CharField(unique=False, max_length=255, default='Mohit Gupta')


    def __str__(self):
        return f'{self.figure_no}  -  {self.library_name}  -  {self.heading})'


    def get_absolute_url(self):
        # Reverse will take you back and forth to the visualization detail
        # that you will click
        return reverse('dsrs_viz_d3_react_js_detail_urlpattern',
                       kwargs={'pk':self.pk}
                       )

    def get_update_url(self):
        return reverse('dsrs_viz_d3_react_js_update_urlpattern',
                       kwargs={'pk':self.pk})



    class Meta:
        ordering = ['figure_no', 'library_name', 'heading']
        unique_together = ['figure_no', 'library_name', 'heading']