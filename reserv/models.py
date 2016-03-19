from __future__ import unicode_literals
from datetime import time
from pip import logger
from time import sleep
import urllib2

from django.db import models

# Create your models here.
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.proxy import *
from pyvirtualdisplay import Display
from visareserv.constatnts import *
import pyautogui


class DateChecker(models.Model):
    url = models.URLField(max_length=500)
    name = models.CharField(max_length=200, blank=True, null=True, help_text='Name of company.')
    nationality = models.CharField(choices=NATIONALITY_CHOICE, max_length=20, blank=False, null=True, default=UKRAINE)
    status = models.CharField(choices=STATUS_CHOICE, max_length=20, blank=False, null=True, default='UKRAINE')
    period = models.IntegerField(default=10, help_text='Max count parsed object per day.')


    def init(self):
        regex = '<img src="/flags/png/ua.png" title="(.+?)" />'
        html = urllib2.urlopen("http://myip.com.ua/").read()
        result_1 = re.findall(regex, html)
        print "my OLD ip is", result_1
        try:
            self.display = Display(visible=0, size=(1024, 768))
            #self.display.start() # uncoment for server
        except Exception, e:
            logger.error(e, exc_info=True, extra={'Message': 'Cant start display.'})

        # try:
        #     self.driver = webdriver.Firefox()
        #     # self.driver
        #     self.driver.implicitly_wait(1)
        # except Exception, e:
        #     logger.error(e, exc_info=True, extra={'Message': 'Cant start browser.'})
        #     self.display.stop()
        # logger.debug("Init: good.")
        # return True
        # proxyHost = "188.191.33.126"
        # proxyPort = "3128"

        try:
            fp = webdriver.FirefoxProfile()
            proxyHost = "85.214.127.112"
            proxyPort = "3128"
            # proxyHost = "37.46.129.238"
            # proxyPort = "8080"
            # proxyHost = "85.143.164.100"
            # proxyPort = "81"


            fp.set_preference("network.proxy.type", 1)
            fp.set_preference("network.proxy.http", proxyHost) #HTTP PROXY
            fp.set_preference("network.proxy.http_port", int(proxyPort))
            fp.set_preference("network.proxy.ssl", proxyHost) #SSL  PROXY
            fp.set_preference("network.proxy.ssl_port", int(proxyPort))
            fp.set_preference('network.proxy.socks', proxyHost) #SOCKS PROXY
            fp.set_preference('network.proxy.socks_port', int(proxyPort))
            fp.set_preference('webdriver_enable_native_events', False)

            fp.update_preferences()
            self.driver = webdriver.Firefox(fp)#

            # print "1"
            # self.driver.get("http://myip.com.ua/")# https://2ip.com.ua/ru
            print "2"
            # # self.driver.implicitly_wait(1)
            # print "3"
            # html = (self.driver.page_source).encode('utf-8')
            # print "4"
            # regex = 'value="(.+?)" maxlength'
            # result_2 = re.findall(regex, html)
            # print "my NEW ip is", result_2

        # try:
        #     from selenium.webdriver.common import proxy, desired_capabilities
        #     from selenium.webdriver.firefox import webdriver
        #
        #     p = proxy.Proxy({
        #         'proxyType': proxy.ProxyType().MANUAL,
        #         'httpProxy': '85.143.164.100:81',
        #         })
        #
        #     capabilities = desired_capabilities.DesiredCapabilities().FIREFOX
        #     p.add_to_capabilities(capabilities)
        #     self.driver = webdriver.WebDriver(capabilities=capabilities)

        except Exception, e:
            logger.error(e, exc_info=True, extra={'Message': 'Cant start browser.'})
            self.display.stop()
        logger.debug("Init: good.")
        return True

    # def hover(self):
    #     wd = self.webdriver_connection.connection
    #     element = wd.find_element_by_class_name("recaptcha-checkbox-hover")
    #     hov = self.ActionChains(wd).move_to_element(element)
    #     hov.perform()

    def get_number_image(self, result):
        res = []
        if " " in result:
            result = result.replace(' ', '')
        if ',' in result:
            result = result.replace(',', '')
        if '.' in result:
            result = result.replace('.', '')
        try:
            for char in result:
                res.append(int(char))
        except:
            print "problem at ress.append(int(char))"
        return res

    def get_coordinate(self, all_number):
        coordinate = [
            [1, 690, 345],
            [2, 818, 340],
            [3, 945, 353],
            [4, 699, 471],
            [5, 818, 479],
            [6, 945, 465],
            [7, 692, 598],
            [8, 816, 598],
            [9, 946, 612],
            ]
        coord = []
        for numb in coordinate:
            for r in all_number:
                if r == numb[0]:
                    coord.append([numb[1], numb[2]])
        return coord


    def click_on_image(self, coordinate):
        for coord in coordinate:
            x, y = coord[0], coord[1]
            try:
                pyautogui.click(x=x, y=y)
            except Exception, e:
                print e
        self.driver.find_element_by_xpath('//*[@id="rc-imageselect-target"]/table/tbody/tr[1]/td[1]/div').click()
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="rc-imageselect-target"]/table/tbody/tr[1]/td[2]/div').click()
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="rc-imageselect-target"]/table/tbody/tr[2]/td[1]/div').click()
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="rc-imageselect-target"]/table/tbody/tr[2]/td[2]/div').click()


    def main_func(self):
            pyautogui.click(x=771, y=573)
            is_ok = False
            while is_ok!=True:
                if self.status != STOP:
                    sleep(5)
                    pyautogui.moveTo(x=100, y=100)
                    self.driver.save_screenshot('/home/myroslav/reserv/reserv/visareserv/screenshot/screed/1'+'.png')

                    from PIL import Image
                    test_image = "/home/myroslav/reserv/reserv/visareserv/screenshot/screed/1.png"
                    original = Image.open(test_image)
                    box = (569, 89, 982, 596)
                    cropped_example = original.crop(box)
                    cropped_example.save("/home/myroslav/reserv/reserv/visareserv/screenshot/res/1.png", 'png')

                    from antigate import AntiGate
                    gate = AntiGate('AntiGatePass')
                    captcha_id = gate.send("/home/myroslav/reserv/reserv/visareserv/screenshot/res/1.png")
                    result = gate.get(captcha_id)
                    print result
                    if result:
                        all_number = self.get_number_image(result)
                        print "all_number", all_number
                        coordinate = self.get_coordinate(all_number)
                        print "coordinate", coordinate
                        self.click_on_image(coordinate)
                        pyautogui.click(x=954, y=706)
                        pyautogui.moveTo(710, 657, 3, pyautogui.easeInOutQuad)
                        pyautogui.click(x=710, y=657)

                        text = self.driver.find_element_by_xpath('//*[@id="cp1_lblNoDates"]').text
                        print text
                        print self.driver.find_element_by_xpath('//*[@id="cp1_lblNoDatesEmbassyInfo"]').text
                        #We are sorry, but no free slots are available. Try to register later.
                        # [2016-02-19 00:05:09,402: WARNING/Worker-5] 2/19/2016 12:05:12 AM UTC, Ukraine () - Kyjev, Long-term residence permit

                        if "We are sorry" in text:
                            pyautogui.moveTo(685, 439, 3, pyautogui.easeInOutQuad)
                            pyautogui.click(x=685, y=439)
                            sleep(2)
                            obj = DateCheckerBase(company=self, text=text, free_date=None)
                            obj.save()
                            self.main_func()
                        else:
                            is_ok = True
                            obj = DateCheckerBase(company=self, text=text, free_date=None)
                            obj.save()

    def do(self):
        logger.debug("I'm do it")
        self.init()
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.find_element_by_xpath('//*[@id="ctl00_cp1_btnAccept"]').click()
        self.driver.find_element_by_xpath('//*[@id="ctl00_cp1_btnNewAppointment"]').click()
        self.driver.find_element_by_xpath('//*[@id="ctl00_cp1_ddCitizenship_Input"]').send_keys(self.nationality)
        self.driver.find_element_by_xpath('//*[@id="ctl00_cp1_ddCountryOfResidence_Input"]').click()
        self.driver.find_element_by_xpath('//*[@id="ctl00_cp1_ddVisaType_Input"]').click()
        self.driver.find_element_by_xpath('//*[@id="ctl00_cp1_ddVisaType_DropDown"]/div/ul/li[2]').click()

        try:
            self.main_func()
        except Exception, e:
            print e
            self.driver.close()
            if self.status != STOP:
                self.do()


    def __unicode__(self):
        return self.name


class DateCheckerBase(models.Model):
    company = models.ForeignKey(DateChecker, default=None, blank=True, null=True, help_text='The company that is owner of this element.')
    text = models.CharField(max_length=500, blank=True, null=True, help_text='Example of field for saving some information.')
    date = models.DateTimeField(auto_now_add=True, auto_now=False)
    free_date = models.DateTimeField(auto_now_add=False, auto_now=False, null=True)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return self.name