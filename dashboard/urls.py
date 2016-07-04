from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),
    url(r'^register/$', views.register, name='register'),
    url(r'^homepage/$', 'django.contrib.auth.views.login', {
    	'template_name' : 'dashboard/index.html'
    	}, name='home'),
    url(r'^$', views.landingPage, name='landing_page'),
    url(r'^letsmeet/$', views.showDashboard, name='dashboard'),
    url(r'^___LM_ge___/$', views.getEvents, name='get_events'),
    url(r'^___LM_ae___/$', views.addEvent, name='add_event'),
]


