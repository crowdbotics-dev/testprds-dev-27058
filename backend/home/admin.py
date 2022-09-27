from django.contrib import admin
from .models import Test, Tested

admin.site.register(Tested)
admin.site.register(Test)

# Register your models here.
