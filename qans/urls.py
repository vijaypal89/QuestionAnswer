from django.conf.urls.defaults import *
from project1.qans import views
urlpatterns = patterns('',
	(r'^$', views.basesearch),
	(r'^createUser/$', views.createUser),
	(r'^addquestion/$', views.addq),
	(r'^search/$', views.search),
	(r'^home/$', views.home),
	(r'^profile/$', views.profile),
	(r'^addanswer/(?P<idq>\w+)$', views.addanswer),
	(r'^answer/(?P<idq>\w+)/$', views.answer),
	(r'^invalid/$', views.invalid),
	(r'^login_view/$', views.login_view),
	(r'^logout_view/$', views.logout_view),
)
