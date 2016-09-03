from django.conf.urls import url
from . import views

app_name = 'Exports'

urlpatterns = [
        url(r'^balance/$', views.balance, name='balance'),
        url(r'^accountdata/$', views.accountdata, name='accountdata'),
        url(r'^accountdetail/$', views.accountdetail, name='accountdetail'),
    ]
