from django.contrib import admin
from .models import NewModel, Test, Tested

admin.site.register(Tested)
admin.site.register(Test)
admin.site.register(NewModel)

# Register your models here.
