# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Subject, Teacher, Topic, Post

admin.site.register(Subject)
admin.site.register(Teacher)
admin.site.register(Topic)
admin.site.register(Post)