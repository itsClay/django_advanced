from django.contrib import admin
from blog_drf.models import EntryAPI
from blog_drf.models import TagAPI

# Register your models here.
# This lets us view the Entry and Tag model in the admin panel

admin.site.register(EntryAPI)
admin.site.register(TagAPI)