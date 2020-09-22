from django.conf.urls import url
from . import views

urlpatterns = [
    url('wombats/', views.wombats_view, name="wombat"),
    url('', views.home, name="home"),
]
