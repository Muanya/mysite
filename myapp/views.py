from django.shortcuts import render
from .forms import Contact_form as cf
from django.http import HttpResponseRedirect
from django.urls import reverse
from myapp.models import Project
import requests




# Create your views here.
def home(request):
	contxt = {'template': 'Home', 'title': 'My Django App', 
		'description': 'Welcome to my first an app!'}
	return render(request, 'myapp/index.html', contxt)

def forms(request):

	if request.method == "POST":
		form = cf(request.POST)
		if form.is_valid():
			return HttpResponseRedirect(reverse('form-success-view'))
	else:
		form = cf()

	contxt = {'form': form, 'title':'Form'}

	return render(request, 'myapp/contact_form.html', contxt)

def success_message(request):
	contxt = {'message': " Successfully Sent :)", 'title':'success'}
	return render(request, 'myapp/success.html', contxt)


def project_index(request):
	proj = Project.objects.all()
	contxt = {
		'title': 'List of Projects',
		'projects': proj
	}

	return render(request, 'myapp/project_index.html', contxt)

def project_detail(request, pkey):
	proj =Project.objects.get(pk=pkey)
	contxt = {
		'title': 'List of Projects',
		'project': proj
	}

	return render(request, 'myapp/project_detail.html', contxt)


def question_index(request):
	msg = ""
	title = "QuestionAPI"
	endpoint = "http://127.0.0.1:8000/questions/api/ques/"
	if request.method == "POST":
		data = {'name': request.POST['name'],
				'email': request.POST['email'],
				'message': request.POST['message']}
		msg = requests.post(endpoint, data=data)
		msg = msg.status_code
	contxt ={'title': title, 'msg': msg}

	return render(request, 'myapp/questions.html', contxt)


##  Api for random users
## const url = 'https://randomuser.me/api/?results=10'; // Get 10 random users