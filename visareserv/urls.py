from django.conf.urls import url
from django.contrib import admin
from django.views.generic import RedirectView

urlpatterns = [
    url(r'^$', 'vamiko.views.home', name='home'),
    url(r'^admin/', admin.site.urls),
    url(r'^favicon\.ico$', RedirectView.as_view(url='/static/logo_vectorized.png'),),
    url(r'^form_upload', 'vamiko.views.form_upload', name='form_upload'),
]
