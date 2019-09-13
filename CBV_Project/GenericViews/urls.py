from GenericViews import views
from django.conf.urls import url

app_name = 'GenericViews'

urlpatterns = [
    url(r'^$',views.IndexView.as_view(),name='index'),
    url(r'^(?P<pk>[0-9]+)/$',views.DetailsViews.as_view(),name='detail'),

    url(r'makeentry/$',views.makeentry , name='makeentry'),
]