from django.conf.urls.defaults import *
from project1.practice import views
urlpatterns = patterns('',
	(r'^test1/$', views.base),
	(r'^test2/$', views.test2),
	(r'^test3/$', views.test3),
	(r'^test4/$', views.test4),
)
