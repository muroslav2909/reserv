from __future__ import unicode_literals
from django.core.validators import RegexValidator

from django.db import models


class VisitorMessage(models.Model):
    visitor_name = models.CharField(max_length=50, blank=True, null=True)
    message_text = models.CharField(max_length=5000, blank=False, null=False) # can be TextField
    visitor_email = models.EmailField(max_length=50, blank=False, null=False)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    visitor_phone = models.CharField(max_length=20, blank=True, null=True)
    def __unicode__(self):
        return self.visitor_email

class Subscribe(models.Model):
    visitor_email = models.EmailField(max_length=50, blank=False, null=False)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return self.visitor_email