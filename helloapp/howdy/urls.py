# howdy/urls.py
from django.conf.urls import url
from howdy import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
    url(r'^about/$', views.AboutPageView.as_view()),
    url(r'^city_overview/(?P<city_name>[a-zA-Z]+)$', views.CityOverview.as_view()),
    url(r'^city_roads/(?P<city_name>[a-zA-Z]+)$', views.CityRoads.as_view()),
]
