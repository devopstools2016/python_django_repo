from django.conf.urls import url
from django.contrib import admin
from dateapp import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^date/',views.dateview)
]
