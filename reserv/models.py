from __future__ import unicode_literals
from pip import logger

from django.db import models

# Create your models here.
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.proxy import *
from pyvirtualdisplay import Display
from visareserv.constatnts import *


class DateChecker(models.Model):
    url = models.URLField(max_length=500)
    name = models.CharField(max_length=200, blank=True, null=True, help_text='Name of company.')
    nationality = models.CharField(choices=NATIONALITY_CHOICE, max_length=20, blank=False, null=True, default=UKRAINE)
    status = models.CharField(choices=STATUS_CHOICE, max_length=20, blank=False, null=True, default='UKRAINE')
    period = models.IntegerField(default=10, help_text='Max count parsed object per day.')


    def init(self):
        logger.debug("I'm init.")
        try:
            self.display = Display(visible=0, size=(1024, 768))
            #self.display.start() # uncoment for server
        except Exception, e:
            logger.error(e, exc_info=True, extra={'Message': 'Cant start display.'})

        try:
            self.driver = webdriver.Firefox()
            self.driver.implicitly_wait(100)
        except Exception, e:
            logger.error(e, exc_info=True, extra={'Message': 'Cant start browser.'})
            self.display.stop()
        logger.debug("Init: good.")
        return True

    def do(self):
        logger.debug("I'm do it")
        self.init()
        self.driver.get(self.url)
        self.driver.find_element_by_xpath('//*[@id="ctl00_cp1_btnAccept"]/span[1]').click()
        self.driver.find_element_by_xpath('//*[@id="ctl00_cp1_btnNewAppointment"]/span').click()
        self.driver.find_element_by_xpath('//*[@id="ctl00_cp1_ddCitizenship_Input"]').send_keys(self.nationality)
        self.driver.find_element_by_xpath('//*[@id="ctl00_cp1_ddCitizenship_DropDown"]/div/ul/li[22]').click()
        self.driver.find_element_by_xpath('//*[@id="ctl00_cp1_ddVisaType_DropDown"]/div/ul/li[2]').click()
        self.driver.find_element_by_xpath('//*[@id="ctl00_cp1_btnNext"]/span').click()



    def __unicode__(self):
        return self.name


class DateCheckerBase(models.Model):
    company = models.ForeignKey(DateChecker, default=None, blank=True, null=True, help_text='The company that is owner of this element.')
    text = models.CharField(max_length=500, blank=True, null=True, help_text='Example of field for saving some information.')
    date = models.DateTimeField(auto_now_add=True, auto_now=False)
    free_date = models.DateTimeField(auto_now_add=False, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return self.name