"""
This file defines helper functions used to get events from outlook
"""

from . import outlookservice
from datetime import datetime

"""
returns a list of events converted so that the fullcalendar.js can display events
from outlook too if the user has connected their outlook account
"""
OUTLOOK_TIME_FORMAT_STRING = "%Y-%m-%dT%H:%M:%S.0000000"

def get_events_from_outlook(access_token, email):

	json_list = []

	#get the events from outlook
	events_data = outlookservice.get_events(access_token, email)

	event_list = events_data['value']
	size = len(event_list)

	#format the list so that full calendar can properly use it
	for i in range(0,size):
		start = datetime.strptime(event_list[i]['Start']['DateTime'], OUTLOOK_TIME_FORMAT_STRING)
		end = datetime.strptime(event_list[i]['Start']['DateTime'], OUTLOOK_TIME_FORMAT_STRING)
		title = event_list[i]['Subject']

		json_data = {
			'start' : start,
			'end' : end,
			'title' : title,
		}

		json_list.append(json_data)

	return json_list






