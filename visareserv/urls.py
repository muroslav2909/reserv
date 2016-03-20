from django.conf.urls import url
from django.contrib import admin
from django.views.generic import RedirectView
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from visareserv import settings

urlpatterns = [
    url(r'^$', 'vamiko.views.home', name='home'),
    url(r'^admin/', admin.site.urls),
    url(r'^favicon\.ico$', RedirectView.as_view(url='/static/logo_vectorized.png'),),
    url(r'^form_upload', 'vamiko.views.form_upload', name='form_upload'),
]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
