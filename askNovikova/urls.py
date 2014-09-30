from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from . import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'askNovikova.views.home', name='home'),
    url(r'^/time/', views.current_datetime(request)),

    url(r'^admin/', include(admin.site.urls)),
)
