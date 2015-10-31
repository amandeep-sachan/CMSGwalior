from django.conf.urls import patterns, url
from gwalior import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^about/', views.about, name='about'),
        url(r'^contact/', views.contact, name='contact'),
        url(r'^add_complaint/', views.add_complaint, name='add_complaint'),
        url(r'^status/', views.complaint_status, name='status'),
        # url(r'^register/$', views.register, name='register'),
        # url(r'^login/$', views.user_login, name='login'),
        #url(r'^restricted/', views.restricted, name='restricted'),
        # url(r'^logout/$', views.user_logout, name='logout'),
        )