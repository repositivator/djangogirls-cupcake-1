from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^profile/$', views.user_profile, name = 'profile'),
    url(r'^register/$', views.register, name = 'register'),
    url(r'^logout_view/$', views.logout_view, name = 'logout'),
]


# available url patterns

# ^login/$ [name='login']
# ^logout/$ [name='logout']
# ^password_change/$ [name='password_change']
# ^password_change/done/$ [name='password_change_done']
# ^password_reset/$ [name='password_reset']
# ^password_reset/done/$ [name='password_reset_done']
# ^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$ [name='password_reset_confirm']
# ^reset/done/$ [name='password_reset_complete']
