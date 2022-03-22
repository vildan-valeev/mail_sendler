# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from mail.models import Follower, FollowerGroup

admin.site.register(Follower)
admin.site.register(FollowerGroup)
