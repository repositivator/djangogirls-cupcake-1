from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.cupcake_list, name='cupcake_list'),
    url(r'^cupcake/price/hightolow$', views.price_hightolow, name='price_hightolow'),
    url(r'^cupcake/price/lowtohigh$', views.price_lowtohigh, name='price_lowtohigh'),
    url(r'^cupcake/rating/hightolow$', views.rating_hightolow, name='rating_hightolow'),
    url(r'^cupcake/(?P<pk>\d+)/$', views.cupcake_detail, name='cupcake_detail'),
    url(r'^cupcake/new/$', views.cupcake_new, name = 'cupcake_new'),
]
