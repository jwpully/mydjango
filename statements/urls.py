from django.conf.urls import url
from . import views

app_name = 'Statements'

urlpatterns = [
        url(r'^$', views.index, name='index'),
        url(r'^single/(?P<id>\d+)/$', views.single, name='single'),
        url(r'^balance/$', views.balance, name='balance'),
    ]
