# Create your views here.
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
import datetime
from books.models import *
from practice.models import *
from practice.form import *
from django.contrib import auth
from django.contrib.auth.models import User

def base(request):
	if request.method == 'POST':
		#form = PostForm(request.POST, request.FILES)
		#if form.is_valid():
		#	post = Post(
		#	image = form.cleaned_data['image'],
		#	text = form.cleaned_data['text'],
		#	)
		#	post.save()
		text = request.POST['text']
		image = request.FILES['image']
		mp3 = request.FILES['mp3']
		Post.objects.create(text = text, image = image, mp3=mp3)
		return render_to_response('test1.html', locals())
	return render_to_response('test1.html', locals())

def test2(request):
	
	return render_to_response('test2.html', locals())

def test3(request):
	res="Hello"
	return render_to_response('test1.html', locals())
	#return HttpResponse(res, mimetype='text/plain')

def test4(request):
	return render_to_response('test4.html', locals())
