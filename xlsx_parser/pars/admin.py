from django.contrib import admin

# Register your models here.
from .models import DataRow, Company, Table

admin.site.register(DataRow)
admin.site.register(Company)
admin.site.register(Table)
