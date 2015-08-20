from django.conf.urls import include, url
from django.conf.urls import patterns     # from djg
from django.contrib import admin
admin.autodiscover()                      # from djg


urlpatterns = [
  #url(r'^$', 'mysite.views.home', name='home'),
  url(r'^polls/', include('polls.urls', namespace="polls")),
  url(r'^ogevents/',include('ogevents.urls')),
    url(r'^admin/', include(admin.site.urls)),
    # next 2 are d from djg                    
    url(r'^accounts/login$',  'django.contrib.auth.views.login'),
    url(r'^accounts/logout/$',                                                   'django.contrib.auth.views.logout', {'next_page': '/'}),    
]




# from djg:   urlpatterns = patterns('',
    # url(r'^$', 'mysite.views.home', name='home'),)



