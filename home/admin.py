from django.contrib import admin
from .models import Guest, FAQ, PlusOneGuest

# Register your models here.

admin.site.register(Guest)
admin.site.register(PlusOneGuest)
admin.site.register(FAQ)
