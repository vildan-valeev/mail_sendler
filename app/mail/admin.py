# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import csv
from os import path

from django.conf.urls import url
from django.contrib import admin

# Register your models here.
from django.contrib.admin import ModelAdmin
from django.forms import forms
from django.shortcuts import redirect, render

from mail.admin_inline import TabularInlinePaginated
from mail.models import Follower, FollowerGroup


class FollowerInline(TabularInlinePaginated):
    # model = FollowerGroup.followers.through
    model = Follower
    extra = 0

    show_change_link = True
    readonly_fields = ['id', 'first_name', 'last_name', 'b_date', 'email']
    per_page = 20


class FollowerAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'b_date', 'email']
    list_display_links = ['id', 'first_name', 'last_name']
    # list_filter = ['groups']
    list_filter = ['group']


class CsvImportForm(forms.Form):
    csv_file = forms.FileField()


class FollowerGroupAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']
    inlines = [FollowerInline]

    # filter_horizontal = ['followers']
    change_form_template = 'admin/mail/followergroup/change_form.html'

    def get_urls(self):
        # super(ModelAdmin, self).__init__()
        urls = super(FollowerGroupAdmin, self).get_urls()
        my_urls = [
            url('import-csv/', self.import_csv),
        ]
        return my_urls + urls

    def change_view(self, request, object_id, form_url='', extra_context=None):
        extra_context = extra_context or {}
        extra_context['object_id'] = object_id
        return super(FollowerGroupAdmin, self).change_view(
            request, object_id, form_url, extra_context=extra_context,
        )

    def import_csv(self, request):
        if request.method == "POST":
            print(dir(request),)
            csv_file = request.FILES["csv_file"]
            reader = csv.reader(csv_file)
            print(request.__dict__)
            group = 2
            Follower.objects.bulk_create(
                [Follower(first_name=i[0], last_name=i[1], b_date=i[2], email=i[3], group_id=group) for i in reader])

            self.message_user(request, "Your csv file has been imported")
            return redirect("..")
        form = CsvImportForm()
        payload = {"form": form}
        return render(
            request, "admin/mail/followergroup/csv_form.html", payload
        )


admin.site.register(Follower, FollowerAdmin)
admin.site.register(FollowerGroup, FollowerGroupAdmin)
