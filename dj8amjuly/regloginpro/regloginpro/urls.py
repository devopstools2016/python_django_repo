from django.conf.urls import include, url
from django.contrib import admin
from regloginapp import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^reg/',views.registration_view),
    url(r'^$',views.login_view),
    url(r'^home/',views.success_view)
]
