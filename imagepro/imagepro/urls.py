from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.views.static import serve
from imageapp import views

urlpatterns = [
    url(r'^$', views.hotel_image_view, name = 'image_upload'),
    url('^images/', views.images, name = 'success'),
]

if settings.DEBUG:
    urlpatterns +=[
        url(r'^media/(?P<path>.*)$',serve,{
            'document_root':settings.MEDIA_ROOT,
        }),
    ]
