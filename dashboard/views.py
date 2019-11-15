from django.shortcuts import render

# Create your views here.

'''
def home(request):
	return HttpResponse('<h1>Dashboard homepage</h1>')
'''

#Dummy data 
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

def home(request):
	context = { 'traffic_data' : traffic_data
	}

	return render(request, 'dashboard/home.html', context)


def about(request):
	return render(request, 'dashboard/about.html', {'title' : "About"})


def charts(request):
	return render(request, 'dashboard/charts.html', {'title' : "Charts"})
