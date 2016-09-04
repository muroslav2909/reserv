# coding=utf-8
from audioop import reverse
from django.http import HttpResponse
from django.shortcuts import render, render_to_response, get_object_or_404
from django.template import Context, loader
from django.template import RequestContext
from vamiko.form import VisitorMessageForm, SubscribeForm
from vamiko.models import VisitorMessage, Subscribe, Item
from visareserv.settings import *
from django.core.mail import send_mail


def home(request):
    if request.method == 'GET':
        form = VisitorMessageForm()
        template = loader.get_template('home.html')
        context = Context({
            'DOMAIN_NAME': DOMAIN_NAME
        })
        # return HttpResponse(template.render(context))
        return render_to_response("home.html", RequestContext(request, context))
        # return render(request, 'home.html', context)
    else:
        # print request.POST
        if 'subscribe' in request.POST:
            form = SubscribeForm(request.POST)
            if form.is_valid():
                visitor_email = form.cleaned_data['visitor_email']
                post = Subscribe(visitor_email=visitor_email)
                send_mail('Нова підписка на сайті',
                          'visitor_email: %s' % (
                          visitor_email), visitor_email,
                          [EMAIL_HOST_USER])

                post.save()

        else:
            form = VisitorMessageForm(request.POST)
            if form.is_valid():
                try:
                    visitor_name = form.cleaned_data['visitor_name']
                    message_text = form.cleaned_data['message_text']
                    visitor_email = form.cleaned_data['visitor_email']
                    visitor_phone = form.cleaned_data['visitor_phone']
                    send_mail('Відвідувач залишив повідомлення на сайті',
                              'visitor_name: %s,message_text: %s,visitor_email: %s, visitor_phone: %s' % (
                              visitor_name, message_text, visitor_email, visitor_phone), visitor_email,
                              [EMAIL_HOST_USER])

                    post = VisitorMessage(visitor_name=visitor_name, message_text=message_text, visitor_email=visitor_email, visitor_phone=visitor_phone)
                    post.save()
                except Exception, e:
                    print e
            else:
                print "form.is_NOT_valid():"

    # return render(request, 'home.html')
    return render_to_response("home.html", RequestContext(request, {}))



def form_upload(request):
    if request.method == 'GET':
        form = VisitorMessageForm()
    else:
        form = VisitorMessageForm(request.POST)
        if form.is_valid():
            visitor_name = form.cleaned_data['visitor_name']
            message_text = form.cleaned_data['message_text']
            visitor_email = form.cleaned_data['visitor_email']
            post = VisitorMessage(visitor_name=visitor_name, message_text=message_text, visitor_email=visitor_email)
            send_mail('Відвідувач залишив повідомлення на сайті',
                      'visitor_name: %s,message_text: %s,visitor_email: %s' % (
                      visitor_name, message_text, visitor_email), visitor_email,
                      [EMAIL_HOST_USER])

            post.save()

    # return render(request, 'form_upload.html', {
    #     'form': '',
    # })#
    return render_to_response("form_upload.html", RequestContext(request, {}))


def base_item_view(request):
    context = {
        'DOMAIN_NAME': DOMAIN_NAME,
    }
    if request.method == 'GET':
        return render_to_response("item_template.html", RequestContext(request, context))
    else:
        form = VisitorMessageForm(request.POST)
        if form.is_valid():
            try:
                visitor_name = form.cleaned_data['visitor_name']
                message_text = form.cleaned_data['message_text']
                visitor_email = form.cleaned_data['visitor_email']
                visitor_phone = form.cleaned_data['visitor_phone']

                post = VisitorMessage(visitor_name=visitor_name, message_text=message_text,
                                      visitor_email=visitor_email, visitor_phone=visitor_phone)
                send_mail('Відвідувач залишив повідомлення на сайті', 'visitor_name: %s,message_text: %s,visitor_email: %s, visitor_phone: %s' %(visitor_name, message_text, visitor_email, visitor_phone), visitor_email, [EMAIL_HOST_USER])
                post.save()
            except Exception, e:
                print e
        else:
            print "form.is_NOT_valid():"

    return render_to_response("item_template.html", RequestContext(request, context))

def detail(request, url_item_name):
    item = Item.objects.filter(url_item_name=url_item_name)[0]
    context = {
        'DOMAIN_NAME': DOMAIN_NAME,
        "item": item,
    }

    if request.method == 'GET':
        return render_to_response("item_template.html", RequestContext(request, context))
    else:
        form = VisitorMessageForm(request.POST)
        if form.is_valid():
            try:
                visitor_name = form.cleaned_data['visitor_name']
                message_text = form.cleaned_data['message_text']
                visitor_email = form.cleaned_data['visitor_email']
                visitor_phone = form.cleaned_data['visitor_phone']

                post = VisitorMessage(visitor_name=visitor_name, message_text=message_text,
                                      visitor_email=visitor_email, visitor_phone=visitor_phone)
                send_mail('Відвідувач залишив повідомлення на сайті',
                          'visitor_name: %s,message_text: %s,visitor_email: %s, visitor_phone: %s' % (
                          visitor_name, message_text, visitor_email, visitor_phone), visitor_email,
                          [EMAIL_HOST_USER])

                post.save()
            except Exception, e:
                print e
        else:
            print "form.is_NOT_valid():"
    return render_to_response("item_template.html", RequestContext(request, context))