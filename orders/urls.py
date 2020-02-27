from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^create/(\w+)/$', views.order_create, name='order_create'),
]
