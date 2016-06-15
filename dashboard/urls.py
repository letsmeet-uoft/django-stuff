from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^logout/$', 'django.contrib.auth.views.logout'),
    url(r'^register/$', views.register, name='register'),
    url(r'^accounts/profile/$', views.profile, name='profile'),
    url(r'^$', 'django.contrib.auth.views.login', {
    	'template_name' : 'dashboard/index.html'
    	}),
    url(r'^letsmeet/$', views.LetsMeetView.as_view(), name='letsmeet')


