from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from askMe import views

urlpatterns = patterns('',

    #url(r'^admin/', ),
    url (r'^$', views.landingPage, name='index'),

    url(r'^signup/$', views.signup, name='signup'),

    url(r'^login/$', views.login, name='s'),
)
