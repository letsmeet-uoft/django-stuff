from django.shortcuts import render, render_to_response, redirect
from django.template import RequestContext
from django.http import HttpResponse, Http404
from django.contrib.auth.views import login as django_login
from django.views import generic
from .forms import UserForm, UserProfileForm
from schedule.models import Calendar

# Create your views here.

def login(request):
    pass


def register(request):
    # Like before, get the request's context.
    context = RequestContext(request)
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            calendar = Calendar.objects.get_or_create_calendar_for_object(profile, profile.__str__() + "Calendar")
            registered = True
        else:
            print (user_form.errors, profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render_to_response(
            'register.html',
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered},
            context)

def profile(request):
	pass

def showDashboard(request):
    return redirect('home') if request.user.is_anonymous() else render(request, 'dashboard/main_dashboard.html')

def landingPage(request):
    return redirect('dashboard') if request.user.is_authenticated() else redirect('home')