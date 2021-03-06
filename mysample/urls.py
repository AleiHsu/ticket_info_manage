from django.conf.urls import url

from mysample.apps import MysampleConfig
from . import views
app_name = 'mysample'

urlpatterns = [
    # ex: /mysample/
    url(r'^$', views.index, name='index'),
    url(r'^tables', views.tables, name='tables'),
    url(r'^index', views.index),
    url(r'^navbar', views.navbar, name='navbar'),
    url(r'^register', views.register, name='register'),
    url(r'^charts', views.charts, name='charts'),
    url(r'^cards', views.cards, name='cards'),
    url(r'^forgot-password', views.forgot_password, name='forgot_password')
]