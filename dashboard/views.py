from django.shortcuts import render
from dashboard.models import *;
import json
from django.core.serializers.json import DjangoJSONEncoder

# Create your views here.

#Dummy data
''' 
traffic_data = [
	{
	 	'user' : 'Jack Barker',
	 	'location' : 'USA',
	 	'pages_visited' : '5',
	 	'visit_duration' : '7m10s',
	 	'unique_user' : 'True',
	 	'longest_page_duration' : '3m21s'
	},
	{
	 	'user' : 'Jane Doe',
	 	'location' : 'UGA',
	 	'pages_visited' : '3',
	 	'visit_duration' : '6m19s',
	 	'unique_user' : 'False',
	 	'longest_page_duration' : '2m18s'
	},
	{
	 	'user' : 'Jack Ma',
	 	'location' : 'CHN',
	 	'pages_visited' : '7',
	 	'visit_duration' : '10m2s',
	 	'unique_user' : 'True',
	 	'longest_page_duration' : '1m45s'
	}

]
'''

#querySet


#1
courses_data = Courses.objects.all();
for course in courses_data:
	#print(course.dept + ' ' + str(course.coursenum))
	print(course)

''' 
#2
courses_data = Courses.objects.values('dept', 'coursenum')

for course in courses_data:
	print(course)
'''

print(type(courses_data))
print(len(courses_data))


def home(request):
	context = { 'courses_data' : courses_data
	}

	return render(request, 'dashboard/home.html', context)


def about(request):
	return render(request, 'dashboard/about.html', {'title' : "About"})


def charts(request):
	return render(request, 'dashboard/charts.html', {'title' : "Charts"})
