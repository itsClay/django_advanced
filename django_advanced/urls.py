from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'django_advanced.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^advanced_tactics/', include('advanced_tactics.urls')),
    url(r'^blog/', include('blog.urls')),
    url(r'^api/blog/', include('blog_drf.api.urls')),

     # Route to Angular
    url(r'^angular-blog/$', 'blog.views.angular', name='angular'),
]
