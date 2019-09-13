from django.contrib import admin
from django.conf.urls import url
from calculation_app import views

urlpatterns = [
    url(r'admin/', admin.site.urls),
    url(r'^$', views.input),
    url(r'^calculation_app/output$',views.output),
    url(r'^add$',views.add),
    url(r'^sub$',views.sub),
    url(r'^mul$',views.mul),
    url(r'^div$',views.div),
]
