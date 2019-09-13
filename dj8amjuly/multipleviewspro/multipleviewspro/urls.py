from django.conf.urls import url
from django.contrib import admin
from multipleviewsapp import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^home/',views.home),
    url(r'^contact/',views.contact),
    url(r'^services/',views.services),
    url(r'^feedback/',views.feedback),
    url(r'^$',views.home)
]
