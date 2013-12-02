# Create your views here.
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
import datetime
from books.models import *
from qans.models import *
from django.contrib import auth
from django.contrib.auth.models import User

def invalid(request):
	error = "username is already exist!"
	return render_to_response('invalid.html', locals())

def home(request):
	return render_to_response('search_form.html')

def basesearch(request):
		user = request.user
		if user is not None:
			if user.is_active:	
				usr = QansUserregistration.objects.get(username=user.username)
				return render_to_response('search_form.html', locals())
		return render_to_response('search_form.html')

def createUser(request):
		if request.method == 'POST':
			username = request.POST['username']
			password = request.POST['password']
			firstname = request.POST['firstname']
			lastname = request.POST['lastname']
			email = request.POST['email']
			address1 = request.POST['address1']
			address2 = request.POST['address2']
			country = request.POST['country']
			dob = request.POST['dob']
			if User.objects.filter(username__exact=username):
				return HttpResponseRedirect('/qans/invalid/')
			User.objects.create_user(username=username, password=password, email=email)
			QansUserregistration.objects.create(username=username, password=password, email=email, first_name=firstname,
									last_name=lastname, dob=dob, addr=address1+" "+address2, country=country)
			user = auth.authenticate(username=username, password=password)
			if user is not None:
				usr = QansUserregistration.objects.get(username=username)
				if user.is_active:
					auth.login(request, user)
					return HttpResponseRedirect('/qans/')

def search(request):
	user = request.user
	if 'q' in request.GET:
		if request.GET['q'] != "":
			items = QansQuestion.objects.filter(title__icontains=request.GET['q'])
	else:
		items = {}	
	if user is not None:
		if user.is_active:	
			usr = QansUserregistration.objects.get(username=user.username)
			return render_to_response('header.html', locals())
	return render_to_response('header.html', locals())

def answer(request, idq):
	user = request.user
	question = QansQuestion.objects.get(id = idq)
	answer = question.qansanswer_set.all()
	if user is not None:
		if user.is_active:	
			usr = QansUserregistration.objects.get(username=user.username)
			return render_to_response('answer.html', locals())
	return render_to_response('answer.html', locals())

def login_view(request):
	error = ""
	def errorHandler(error):
		return render_to_response('search_form.html', {'error' : error})
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		if not AuthUser.objects.filter(username__exact=username):
			error = "user is not register"
			return render_to_response('search_form.html', locals())
		user = auth.authenticate(username = username, password = password)
		if user is None:
			error = "username and password does not match"
			return render_to_response('search_form.html', locals())
		if user is not None:
			usr = QansUserregistration.objects.get(username=username)
			user.is_active = 1;
			if user.is_active:
				auth.login(request, user)
				return HttpResponseRedirect('/qans/')

def logout_view(request):
	request.user.is_active = False
	response = auth.logout(request)
	request.session['SESSION_COOKEI_AGE'] = 0
	return HttpResponseRedirect('/qans/')

#def logout_view_search(request):
#	request.user.is_active = False
#	response = auth.logout(request)
#	return HttpResponseRedirect('/qans/search/')

def addq(request):
	user = request.user
	usr = QansUserregistration.objects.get(username=user.username)
	title = request.POST['title']
	question = request.POST['question']
	QansQuestion.objects.create(user = usr, title = title, question = question)
	return render_to_response('search_form.html', locals())

def addanswer(request, idq):
	user = request.user
	usr = QansUserregistration.objects.get(username=user.username)
	quser = QansQuestion.objects.get(id = idq)
	answer = request.POST['qanswer']
	QansAnswer.objects.create(user=usr, quser=quser, answer=answer)
	return render_to_response('header.html', locals())

def profile(request):
	user = request.user
	usr = QansUserregistration.objects.get(username=user.username)
	return render_to_response('profile.html', locals())
