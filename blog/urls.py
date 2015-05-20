from django.conf.urls import url


urlpatterns = [
    # ex: /polls/
    url(r'^$', 'blog.views.home', name='home'),
    url(r'^register/$', 'blog.views.register', name='register'),
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/home'}, name='logged_out'),
    url(r'^profile/$', 'blog.views.profile', name='profile'),
    ]