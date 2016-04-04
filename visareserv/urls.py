import os
from django.conf.urls import url, patterns
from django.contrib import admin
from django.views.generic import RedirectView
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from visareserv import settings
from visareserv.settings import BASE_DIR

urlpatterns = [
    url(r'^$', 'vamiko.views.home', name='home'),
    url(r'^admin/', admin.site.urls),
    url(r'^favicon\.ico$', RedirectView.as_view(url='/static/logo_vectorized.png'),),
    url(r'^form_upload', 'vamiko.views.form_upload', name='form_upload'),
    url(r'^base_item_view', 'vamiko.views.base_item_view', name='base_item_view'),
    url(r'^(?P<url_item_name>.+?)/$', 'vamiko.views.detail', name='detail'),

]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)\
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

SERVER_ENVIRONMENT = os.getenv('RUN_ENV', '')
if SERVER_ENVIRONMENT == 'PROD':
    urlpatterns += patterns('', (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}), )
    urlpatterns += patterns('', (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}), )
#
# if SERVER_ENVIRONMENT == 'DEV':
#     urlpatterns += patterns('', (r'^(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}), )
#     urlpatterns += patterns('', (r'^(?P<path>.*)$', 'django.views.media.serve', {'document_root': settings.MEDIA_ROOT}), )
