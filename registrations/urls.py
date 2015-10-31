from django.conf.urls import patterns, url, include
from registrations import views
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
        url(r'^register/$', views.register, name='register'),
        url(r'^login/$', views.loginrequest, name='login'),
        # url(r'^restricted/', views.restricted, name='restricted'),
        url(r'^logout/$', views.logoutrequest, name='logout'),
        url(r'^password/change/$',
                    auth_views.password_change,
                    name='password_change'),
      url(r'^password/change/done/$',
                    auth_views.password_change_done,
                    name='password_change_done'),
      url(r'^password/reset/$',
                    auth_views.password_reset,
                    name='password_reset'),
      url(r'^password/reset/done/$',
                    auth_views.password_reset_done,
                    name='password_reset_done'),
      url(r'^password/reset/complete/$',
                    auth_views.password_reset_complete,
                    name='password_reset_complete'),
      url(r'^password/reset/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',
                    auth_views.password_reset_confirm,
                    name='password_reset_confirm'),
        url(r'^$', TemplateView.as_view(template_name="direct.html"))

        )


