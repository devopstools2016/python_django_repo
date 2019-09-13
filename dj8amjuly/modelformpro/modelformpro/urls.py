from django.conf.urls import include, url
from django.contrib import admin
from modelformapp import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',views.emp_view)
]
