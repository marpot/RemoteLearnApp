# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import CreateView
from django.shortcuts import render,redirect
from .models import Subject
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class SubjectCreateView(CreateView):
	model = Subject
	fields = ('subject_name')

class TeacherCreateView(CreateView):
	model = Teacher
	fields = ('first_name', 'last_name')

class TopicCreateView(CreateView):
	model = Topic
	fields = ('topic')



#def mainpage(request):
#	return render(request, 'RemoteLearn/mainpage.html', {})
	