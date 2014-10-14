from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from . import views

urlpatterns = patterns('',
    # Examples:
    
    url(r'^time/', views.current_datetime),

    url(r'^test/', views.test),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^', include('askMe.urls')),
)
