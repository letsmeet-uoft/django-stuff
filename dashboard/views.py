from django.shortcuts import render, render_to_response, redirect
from django.template import RequestContext
from django.http import HttpResponse, Http404, JsonResponse
from django.contrib.auth.views import login as django_login
from django.views import generic
from .forms import UserForm, UserProfileForm
from schedule.models import Calendar
import json
from datetime import datetime, timedelta, date
from schedule.forms import EventForm
from .models import UserProfile


# Create your views here.

def addEvent(request):
    if request.method == 'POST':
        return HttpResponse( request.POST)

def getEvents(request):
    if request.is_ajax:
        json_list = []

        date_handler = lambda obj: (
            obj.isoformat()
            if isinstance(obj, datetime)
            or isinstance(obj, date)
            else None
        )

        profile = UserProfile.objects.get(user=request.user)
        user_calendar = Calendar.objects.get_calendar_for_object(profile)
        event_list = user_calendar.events.all()

        for event in event_list:
            json_event = {
                'start' : event.start,
                'end' : event.end,
                'title' : event.title,
            }

            json_list.append(json_event)

        return HttpResponse(json.dumps(json_list, default=date_handler), content_type='application/json')

    else:
        raise Http404

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

    # user not logged in
    if request.user.is_anonymous():
        return redirect('home')

    else: #logged in
        context = RequestContext(request)

        if request.method == 'POST':
            profile = UserProfile.objects.get(user=request.user)
            user_calendar = Calendar.objects.get_calendar_for_object(profile)
            
            event_form = EventForm(data=request.POST)

            if event_form.is_valid:
                #save event in db
                event = event_form.save()
                #add the event to the users calendar
                user_calendar.events.add(event)
            else:
                HttpResponse(event_form.errors)
        else:
            event_form = EventForm()
        return render(request, 'dashboard/main_dashboard.html', {'event_form' : event_form,})

def landingPage(request):
    return redirect('dashboard') if request.user.is_authenticated() else redirect('home')