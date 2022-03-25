from django.contrib import admin
from django.forms import forms
from django.shortcuts import redirect, render
from django.urls import path

from mail.admin_inline import TabularInlinePaginated
from mail.models import Follower, FollowerGroup, HtmlTemplate, EmailSendler
from mail.services.saving_csv import save_csv


class FollowerInline(TabularInlinePaginated):
    # model = FollowerGroup.followers.through
    model = Follower
    # extra = 0

    show_change_link = True
    readonly_fields = ['id', 'first_name', 'last_name', 'b_date', 'email']
    per_page = 100


class FollowerAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'b_date', 'email']
    list_display_links = ['id', 'first_name', 'last_name']
    # list_filter = ['groups']
    list_filter = ['group']
    readonly_fields = ['created']


class CsvImportForm(forms.Form):
    csv_file = forms.FileField()


class FollowerGroupAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']
    inlines = [FollowerInline]
    # filter_horizontal = ['followers']
    change_form_template = 'admin/mail/followergroup/change_form.html'
    # group_id = None

    # save_on_top = True

    # def get_form(self, request, obj=None, **kwargs):
    #     """Переопределение. Прокидываем атрибут group_id в import_csv для использования в создании Follower"""
    #     if obj:
    #         print(obj.id)
    #         self.group_id = obj.id
    #
    #     return super().get_form(request, obj, **kwargs)

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('<path:object_id>/change/import-csv/', self.import_csv),
        ]
        return my_urls + urls

    def import_csv(self, request, *args, **kwargs):
        print(args, kwargs)
        if request.method == "POST":

            csv_file = request.FILES["csv_file"]
            # TODO: add to celery tasks
            text, level = save_csv(csv_file, kwargs.get('object_id'))
            self.message_user(request, text, level)
            return redirect("..")
        form = CsvImportForm()
        payload = {"form": form}
        return render(
            request, "admin/mail/followergroup/csv_form.html", payload
        )


class HtmlTemplateAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


class EmailSendlerAdmin(admin.ModelAdmin):
    list_display = ['id', 'subject']


admin.site.register(Follower, FollowerAdmin)
admin.site.register(EmailSendler, EmailSendlerAdmin)
admin.site.register(HtmlTemplate, HtmlTemplateAdmin)
admin.site.register(FollowerGroup, FollowerGroupAdmin)
