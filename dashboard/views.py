from django.shortcuts import render, render_to_response, redirect
from django.template import RequestContext
from django.http import HttpResponse, Http404, JsonResponse
from django.contrib.auth.views import login as django_login
from django.views import generic
from django.core.urlresolvers import reverse
from .forms import UserForm, UserProfileForm
from schedule.models import Calendar
import json
from datetime import datetime, timedelta, date
from schedule.forms import EventForm
from .models import UserProfile
from .authhelper import get_signin_url, get_token_from_code, get_user_email_from_id_token
from . import outlookservice
from .outlook_event_helper import get_events_from_outlook
# Create your views here.

connected_to_outlook = False

def event_details(request, event_name):
    if event_name is not None:
        return HttpResponse(event_name)
    else:
        return HttpResponse('outlook or google event')

def pricingPage(request):
    return render(request, 'Pricing.html')

def features(request):
    return render(request, 'features.html')

def addEvent(request):
    if request.method == 'POST':
        return HttpResponse( request.POST)

def getEvents(request):
    import pdb
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
                'url' : reverse('view_event_details', args=[event.title]),
            }

            json_list.append(json_event)

        """
        Check if the user has connected to outlook, and if so append the events 
        from their outlook to the list of events: json_list so that they are also 
        seen on the calendar
        """

        outlook_list = get_events_from_outlook(request.session['outlook_access_token'], request.session['outlook_user_email'])

        json_list = json_list + outlook_list

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
    try:
        user_email = request.session['outlook_user_email']
        access_token = request.session['outlook_access_token']
    except KeyError:
        pass

    if request.user.is_anonymous():
        return redirect('home')

    else: #logged in
        context = RequestContext(request)

        redirect_uri = request.build_absolute_uri(reverse('gettoken'))
        signin_url = get_signin_url(redirect_uri)

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
        return render(request, 'dashboard/main_dashboard.html', {'event_form' : event_form,'signin_url' : signin_url,})

def landingPage(request):
    return redirect('dashboard') if request.user.is_authenticated() else redirect('home')

# testing outlook authentication
def home(request):

    return HttpResponse('<a href="' + signin_url +'">Click here to sign in and view your mail</a>')

# get
def gettoken(request):
    auth_code = request.GET['code']
    redirect_uri = request.build_absolute_uri(reverse('gettoken'))
    token = get_token_from_code(auth_code, redirect_uri)
    access_token = token['access_token']
    user_email = get_user_email_from_id_token(token['id_token'])

    # Save the token in the session
    request.session['outlook_access_token'] = access_token
    request.session['outlook_user_email'] = user_email
    connected_to_outlook = True
    return redirect('dashboard')