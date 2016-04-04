register = template.Library()
from django import template
@register.inclusion_tag('contacts.html')
def show_contacts():
    # reviews = reviews.filter(language=language)
    # path_default_img = str(STATIC_PREFIX)+'images/tutor_default.png'
    return {'reviews': ''}
