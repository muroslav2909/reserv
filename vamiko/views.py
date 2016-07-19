from audioop import reverse
from django.http import HttpResponse
from django.shortcuts import render, render_to_response, get_object_or_404
from django.template import Context, loader

from vamiko.form import VisitorMessageForm, SubscribeForm
from vamiko.models import VisitorMessage, Subscribe, Item
from visareserv.settings import *


def home(request):
    if request.method == 'GET':
        form = VisitorMessageForm()
        template = loader.get_template('home.html')
        context = Context({
            'DOMAIN_NAME': DOMAIN_NAME
        })
        return HttpResponse(template.render(context))
    else:
        # print request.POST
        if 'subscribe' in request.POST:
            form = SubscribeForm(request.POST)
            if form.is_valid():
                visitor_email = form.cleaned_data['visitor_email']
                post = Subscribe(visitor_email=visitor_email)
                post.save()

        else:
            form = VisitorMessageForm(request.POST)
            if form.is_valid():
                try:
                    visitor_name = form.cleaned_data['visitor_name']
                    message_text = form.cleaned_data['message_text']
                    visitor_email = form.cleaned_data['visitor_email']
                    visitor_phone = form.cleaned_data['visitor_phone']

                    post = VisitorMessage(visitor_name=visitor_name, message_text=message_text, visitor_email=visitor_email, visitor_phone=visitor_phone)
                    print post
                    post.save()
                except Exception, e:
                    print e
            else:
                print "form.is_NOT_valid():"
    return render(request, 'home.html')



def form_upload(request):
    if request.method == 'GET':
        form = VisitorMessageForm()
    else:
        form = VisitorMessageForm(request.POST)
        if form.is_valid():
            visitor_name = form.cleaned_data['visitor_name']
            message_text = form.cleaned_data['message_text']
            visitor_email = form.cleaned_data['visitor_email']
            print "visitor_email",visitor_email
            post = VisitorMessage(visitor_name=visitor_name, message_text=message_text, visitor_email=visitor_email)
            post.save()

    return render(request, 'form_upload.html', {
        'form': '',
    })#


def base_item_view(request):
    context = {
        'DOMAIN_NAME': DOMAIN_NAME,
    }

    return render(request, 'item_template.html', context)

def detail(request, url_item_name):
    item = Item.objects.filter(url_item_name=url_item_name)[0]
    context = {
        'DOMAIN_NAME': DOMAIN_NAME,
        "item": item,
    }

    return render(request, 'item_template.html', context)