from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /polls/
    url(r'', views.user_view, name='user_view')
    ]