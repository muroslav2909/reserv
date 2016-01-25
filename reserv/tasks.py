#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import
from celery import task
from reserv.models import DateChecker


@task()
def check_date(company_id):
    # print "I'm in selery 1"
    # rdb.set_trace()
    # print "I'm in selery 2"
    p = DateChecker.objects.get(id=company_id)
    print "do(): %s " % str(p.do())