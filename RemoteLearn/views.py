# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic import CreateView
from django.shortcuts import render

from .models import Subject

class SubjectCreateView(CreateView):
	model = Subject
	fields = ('subject_name')
