from __future__ import unicode_literals
from django.core.validators import RegexValidator
# -*- coding: utf-8 -*-
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


class Item(models.Model):
    item_name = models.CharField(max_length=500, blank=False, null=False, help_text="item name")
    url_item_name = models.CharField(max_length=500, blank=True, null=True, help_text="item url name. latin symbols!")
    description_one = models.TextField(max_length=5000, blank=True, null=True, help_text="What it is. For what. What are the materials.")
    description_two = models.TextField(max_length=5000, blank=True, null=True, help_text="Dimensions. Production time.")
    price = models.IntegerField(blank=False, null=False, help_text="Price")
    detail_description_one = models.TextField(max_length=5000, blank=True, null=True, help_text="other description #1")
    detail_description_two = models.TextField(max_length=5000, blank=True, null=True, help_text="other description #2")
    title = models.CharField(max_length=500, blank=False, null=False, help_text="title page")
    meta_description = models.CharField(max_length=500, blank=False, null=False, help_text="meta description")
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    image_one = models.ImageField(upload_to='', default=None)
    image_two = models.ImageField(upload_to='', default=None, blank=True, null=True)
    image_tree = models.ImageField(upload_to='', default=None, blank=True, null=True)
    image_four = models.ImageField(upload_to='', default=None, blank=True, null=True)
    def __unicode__(self):
        return self.item_name