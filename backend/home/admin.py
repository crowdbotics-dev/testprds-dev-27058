from django.contrib import admin
from .models import NewModel, Tested

admin.site.register(Tested)
admin.site.register(NewModel)

# Register your models here.
