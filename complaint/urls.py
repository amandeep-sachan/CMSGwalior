from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from gwalior import views

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'gwalior.views.index', name='index'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^gwalior/', include('gwalior.urls')),
    url(r'^registrations/', include('registrations.urls')),
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^profile/$', 'registrations.views.profile', name='profile'),
)

if settings.DEBUG:
	urlpatterns += patterns(
		'django.views.static',
		(r'^media/(?P<path>.*)',
			'serve',
			{'document_root': settings.MEDIA_ROOT}),
		)
