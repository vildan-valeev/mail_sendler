# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.
from django.utils.encoding import python_2_unicode_compatible


class BaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True, editable=False, null=True)

    class Meta:
        abstract = True


@python_2_unicode_compatible
class Follower(BaseModel):
    """Список подписчиков"""
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    b_date = models.DateTimeField()
    email = models.EmailField()
    group = models.ForeignKey('FollowerGroup', on_delete=models.CASCADE)

    def __str__(self):
        return '{} | {} {}'.format(self.id, self.first_name, self.last_name)


@python_2_unicode_compatible
class FollowerGroup(BaseModel):
    """Группы подписчиков для рассылки"""
    name = models.CharField(max_length=200)

    # followers = models.ManyToManyField('Follower', related_name='groups')

    def __str__(self):
        return '{} | {}'.format(self.id, self.name)


@python_2_unicode_compatible
class HtmlTemplate(BaseModel):
    """"""
    name = models.CharField(max_length=100)
    html_template = models.FileField(upload_to='html_templates')

    # Шаблон без изображений. Если требуется изображения, то создаем отдельную модель подгружаем, тут привязываем M2M
    # images = ...

    def __str__(self):
        return '{} | {}'.format(self.id, self.name)


@python_2_unicode_compatible
class EmailSendler(BaseModel):
    from_email = models.EmailField()
    subject = models.CharField(max_length=78)
    text = models.TextField(max_length=3000)
    # Если html НЕ вставлен, то отправляется только текст.
    # Если вставлен, то обработка шаблона перед отправкой каждому Follower
    follower_group = models.ForeignKey(FollowerGroup, on_delete=models.PROTECT, blank=True, null=True)
    html_template = models.ForeignKey(HtmlTemplate, on_delete=models.PROTECT, blank=True, null=True, related_name='sendlers')
    # attach = models.FileField()
    delayed = models.DateTimeField(help_text='Choose time when need to send emails,', blank=True, null=True)

    def __str__(self):
        return '{} | {}'.format(self.id, self.subject)
