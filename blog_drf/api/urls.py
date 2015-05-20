from django.conf.urls import url
from blog_drf.api.views.entry_view import EntryView

urlpatterns = [
    url(r'^entries/$', EntryView)
]