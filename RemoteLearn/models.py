# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User

from django.contrib.auth.models import timezone

class Subject(models.Model):
	subject_name = models.CharField(max_length=50)
	on_delete  = models.CASCADE


class Teacher(models.Model):
	imie = models.CharField(max_length=30)
	nazwisko = models.CharField(max_length=30)

class Topic(models.Model):
	subject = models.CharField(max_length=255)
	last_updated = models.DateTimeField(auto_now_add=True)
	
	#starter = models.ForeignKey(User, related_name='topics')

class Post(models.Model):
	author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True , null=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title