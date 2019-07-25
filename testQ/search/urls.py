from django.conf.urls import url, include
from . import views

urlpatterns = [
    url( r'^$', views.index, name = 'demo_index' ),
    url( r'^users/', views.ajax_user_search, name = 'demo_user_search' ),
]