import os
from django.contrib import admin
from models import VisitorMessage, Subscribe, Item
from visareserv.settings import *

class VisitorMessageAdmin(admin.ModelAdmin):
    list_display = ["id", "__unicode__", "visitor_name", "visitor_phone","message_text", "created", "updated"]
    list_search = ("visitor_email", "visitor_name", "visitor_phone")

admin.site.register(VisitorMessage, VisitorMessageAdmin)

class SubscribeAdmin(admin.ModelAdmin):
    list_display = ["id", "__unicode__", "created", "updated"]
    list_search = ("visitor_email")

admin.site.register(Subscribe, SubscribeAdmin)

class ItemAdmin(admin.ModelAdmin):
    list_display = ["id", "__unicode__", "url_item_name", "preview_image_url", "price", "title", "meta_description",
                    "description_one", "description_two", "detail_description_one", "detail_description_two",
                    "image_one", "image_two", "image_tree", "image_four", "created", "updated"]
    list_search = ("item_name", "title")

    def preview_image_url(self, item):
        image_path = os.path.join(BASE_DIR + "/")
        # return image_path
        # image_path = image_path.replace('\\','/') # Windows-Fix
        # return '<img src="' + image_path + str(item.image_one) +'"/></a>'
        # https://ucarecdn.com/92d56a14-d5e9-4fd1-8d61-65ee4b3e8c95/added_resume_field.png
        DOMAIN_NAME = 'http://127.0.0.1:8000'
        return '<img src="'+image_path + str(item.image_one) +'"/></a>'



        #<a href="'+ image_path + str(item.image_one) +'/">
        # return '<a href="'+ DOMAIN_NAME + str(item.image_one) + '"/></a>'
        # return '<a href="'+ str(item.image_one) +'/"><img src="'+ str(item.image_one) +'"/></a>'

    # preview_image_url.short_description = 'Thumbnail'
    preview_image_url.allow_tags = True

admin.site.register(Item, ItemAdmin)