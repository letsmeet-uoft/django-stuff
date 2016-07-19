from django.conf.urls import url

from . import views
app_name = 'dashboard'
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
    url(r'^Pricing/$', views.pricingPage, name='Pricing'),
    url(r'^Features/$', views.features, name='Features'),
    url(r'^event/(?P<event_name>.*)$', views.event_details, name='view_event_details'),

    #temp urls to test using outlook rest apis
    
    url(r'^gettoken/$', views.gettoken, name='gettoken'),
]


