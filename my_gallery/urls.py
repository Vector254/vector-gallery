from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve


urlpatterns=[
    url('^$',views.welcome,name = 'welcome'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^location/(?P<location>\w+)/', views.image_location, name='location'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT),
if not settings.DEBUG:
    urlpatterns += [ url(r'^uploads/(?P<path>.)$', serve,{'document_root': settings.MEDIA_ROOT}), url(r'^static/(?P<path>.)$', serve,{'document_root': settings.STATIC_ROOT}), ]