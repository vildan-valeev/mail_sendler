# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


# Create your models here.
class BaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True, editable=False, null=True)

    class Meta:
        abstract = True


class Follower(BaseModel):
    """Список подписчиков"""
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    b_date = models.DateTimeField()
    email = models.EmailField()
    group = models.ForeignKey('FollowerGroup', on_delete=models.CASCADE)

    def __str__(self):
        return '{} | {} {}'.format(self.id, self.first_name, self.last_name)


class FollowerGroup(BaseModel):
    """Группы подписчиков для рассылки"""
    name = models.CharField(max_length=200)
    # followers = models.ManyToManyField('Follower', related_name='groups')

    def __str__(self):
        return '{} | {}'.format(self.id, self.name)
