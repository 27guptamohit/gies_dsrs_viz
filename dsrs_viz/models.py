from django.db import models

class D3_js(models.Model):
    figure_no = models.AutoField(primary_key=True)
    library_name = models.CharField(unique=False, max_length=255)
    heading = models.TextField(unique=True)
    description = models.TextField(unique=False)
    js_code = models.TextField(unique=False)

    def __str__(self):
        return f'{self.figure_no}  -  {self.library_name}  -  {self.heading})'

    class Meta:
        ordering = ['figure_no', 'library_name', 'heading']
        unique_together = ['figure_no', 'library_name', 'heading']



class React_js(models.Model):
    figure_no = models.AutoField(primary_key=True)
    library_name = models.CharField(unique=False, max_length=255)
    heading = models.TextField(unique=True)
    description = models.TextField(unique=False)
    js_code = models.TextField(unique=False)

    def __str__(self):
        return f'{self.figure_no}  -  {self.library_name}  -  {self.heading})'

    class Meta:
        ordering = ['figure_no', 'library_name', 'heading']
        unique_together = ['figure_no', 'library_name', 'heading']



class D3_react_js(models.Model):
    figure_no = models.AutoField(primary_key=True)
    library_name = models.CharField(unique=False, max_length=255)
    heading = models.TextField(unique=True)
    description = models.TextField(unique=False)
    js_code = models.TextField(unique=False)

    def __str__(self):
        return f'{self.figure_no}  -  {self.library_name}  -  {self.heading})'

    class Meta:
        ordering = ['figure_no', 'library_name', 'heading']
        unique_together = ['figure_no', 'library_name', 'heading']