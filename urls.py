from django.conf.urls.defaults import *
from project1.views import *
from django.conf import settings
from project1.books import views 
from project1.qans import views 
from django.contrib.auth.views import *
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	(r'^qans/', include('project1.qans.urls')),
	(r'^test/', include('project1.practice.urls')),
	(r'^date/$', current_date),
	(r'^future/(\d+)$', future_date),
	(r'^acc/$', logout_view),
#	(r'^$', login_view),

    # Example:
    # (r'^project1/', include('project1.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
     (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     (r'^admin/', include(admin.site.urls)),
)
if settings.DEBUG:
	urlpatterns += patterns('django.views.static',
		(r'^%s(?P<path>.*)$' % (settings.MEDIA_URL[1:],), 'serve', {
			'document_root': settings.MEDIA_ROOT,
			'show_indexes': True }),)
