# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import csv

from django.conf.urls import url
from django.contrib import admin
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
    group_id = None

    def get_form(self, request, obj=None, **kwargs):
        """Переопределние. Прокидываем атрибут group_id в import_csv для использования в создании Follower"""
        if obj:
            self.group_id = obj.id
        return super(FollowerGroupAdmin, self).get_form(request, obj, **kwargs)

    def get_urls(self):
        urls = super(FollowerGroupAdmin, self).get_urls()
        my_urls = [
            url('import-csv/', self.import_csv),
        ]
        return my_urls + urls

    def import_csv(self, request):
        if request.method == "POST":
            print("POST", request.POST,)
            csv_file = request.FILES["csv_file"]
            reader = csv.reader(csv_file)
            Follower.objects.bulk_create(
                [Follower(first_name=i[0], last_name=i[1], b_date=i[2], email=i[3], group_id=self.group_id) for i in
                 reader])
            self.message_user(request, "Your csv file has been imported")
            return redirect("..")
        form = CsvImportForm()
        print('кукана')
        payload = {"form": form}

        return render(
            request, "admin/mail/followergroup/csv_form.html", payload
        )


admin.site.register(Follower, FollowerAdmin)
admin.site.register(FollowerGroup, FollowerGroupAdmin)
