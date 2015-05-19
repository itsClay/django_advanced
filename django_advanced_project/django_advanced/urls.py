from django.conf.urls import include, url
from django.contrib import admin
from advanced_tactics import urls as at_urls

urlpatterns = [
    # Examples:
    # url(r'^$', 'django_advanced.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^advanced_tactics/', include(at_urls))
]
