from django.conf.urls import url
from . import views

app_name = 'Processes'

urlpatterns = [
#        url(r'^$', views.index, name='index'),
#        url(r'^single/(?P<id>\d+)/$', views.single, name='single'),
        url(r'^chargeowners/$', views.chargeowners, name='chargeowners'),
        url(r'^latefees/$', views.latefees, name='latefees'),
        url(r'^accesscontrol/$', views.accesscontrol, name='latefees'),
    ]
