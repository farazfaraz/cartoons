from django.contrib import admin

# Register your models here.
from HindiCartoon.models import Cartoon,Episode, Season

admin.site.register(Cartoon)
admin.site.register(Episode)
admin.site.register(Season)
