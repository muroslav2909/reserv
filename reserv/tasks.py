#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import
from celery import task
from reserv.models import DateChecker
from selenium import webdriver

@task()
def check_date(company_id):
    p = DateChecker.objects.get(id=company_id)
    p.do()
    print "do(): %s " % p.name

@task()
def stop():
    driver = DateChecker.driver
    #driver = webdriver.Firefox()
    driver.close()