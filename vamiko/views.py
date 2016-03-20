from audioop import reverse
from django.shortcuts import render, render_to_response

from vamiko.form import VisitorMessageForm, SubscribeForm
from vamiko.models import VisitorMessage, Subscribe


def home(request):
    if request.method == 'GET':
        form = VisitorMessageForm()
    else:
        print request.POST
        if 'subscribe' in request.POST:
            form = SubscribeForm(request.POST)
            if form.is_valid():
                visitor_email = form.cleaned_data['visitor_email']
                post = Subscribe(visitor_email=visitor_email)
                post.save()

        else:
            form = VisitorMessageForm(request.POST)
            if form.is_valid():
                visitor_name = form.cleaned_data['visitor_name']
                message_text = form.cleaned_data['message_text']
                visitor_email = form.cleaned_data['visitor_email']
                post = VisitorMessage(visitor_name=visitor_name, message_text=message_text, visitor_email=visitor_email)
                post.save()
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
    })
