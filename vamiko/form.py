from django.forms import ModelForm
from vamiko.models import VisitorMessage

#
# class VisitorMessageForm(ModelForm):
#     class Meta:
#         model = VisitorMessage
#         fields = ['visitor_name', 'message_text', 'visitor_email'


from django import forms

class VisitorMessageForm(forms.Form):
    visitor_name = forms.CharField()
    message_text = forms.CharField()
    visitor_email = forms.EmailField()

class SubscribeForm(forms.Form):
    visitor_email = forms.EmailField()


