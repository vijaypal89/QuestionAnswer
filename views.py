from django.shortcuts import render_to_response
import datetime
from books.models import *
from django.contrib import auth
from django.contrib.auth.models import User

def current_date(request):
	current = datetime.datetime.now()
	return render_to_response('current.html', locals())
def future_date(request, offset):
	hour_offset = int(offset)
	next_time = datetime.datetime.now() + datetime.timedelta(hours = hour_offset)
	return render_to_response('future.html', locals())

def logout_view(request):
	authLogout(request)
	return render_to_response('logout.html')

def login_view(request):
	def errorHandler(error):
		return render_to_response('login.html', {'error' : error})
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = auth.authenticate(username = username, password = password)
		if user is not None:
			if user.is_active:
				auth.login(request, user)
				fullName = user.get_full_name
				return render_to_response('logout.html', {'user': user})
			else:
				error = 'Account disabled.'
				return errorHandler(error)
		else:
			error = 'Invalid details entered.'
			return errorHandler(error)

	return render_to_response('login.html')

#@login_required


