from pip import logger
from django.contrib import admin

# Register your models here.
from models import DateChecker
from models import DateCheckerBase
from tasks import *
from visareserv.constatnts import *


class DateCheckerAdmin(admin.ModelAdmin):
    list_display = ["id", "__unicode__", "url", "nationality", "status", "period"]

    list_filter = ("nationality", "status")

    def run(self, request, queryset):

           try:
                if queryset.count() > 1:
                    self.message_user(request, "Choose only one campaign")
                else:
                    campaign = queryset[0]
                    check_date.delay(campaign.id)
                    campaign.status = RUN
                    campaign.save()
           except Exception, e:
                logger.warning(e, exc_info=True )
           self.message_user(request, "Campaign start")

    def stop(self, request, queryset):
           try:
                if queryset.count() > 1:
                    self.message_user(request, "Choose only one campaign")
                else:
                    campaign = queryset[0]
                    #stop.delay()
                    campaign.status = STOP
                    campaign.save()
           except Exception, e:
                logger.warning(e, exc_info=True )
           self.message_user(request, "Campaign start")

    actions = [run, stop]


class DateCheckerBaseAdmin(admin.ModelAdmin):
    list_display = ["id", "company", "text", "free_date", "date", "updated"]

    list_filter = ('company', 'date')

admin.site.register(DateChecker, DateCheckerAdmin)
admin.site.register(DateCheckerBase, DateCheckerBaseAdmin)