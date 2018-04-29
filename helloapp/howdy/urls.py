# howdy/urls.py
from django.conf.urls import url
from howdy import views

urlpatterns = [
    path('/', views.lookup_city, name='lookup-city'),
    # url(r'^$', views.HomePageView.as_view()),
    url(r'^about/$', views.AboutPageView.as_view()),
    url(r'^city_overview/$', views.CityOverview.as_view()),
    url(r'^city_roads/$', views.CityRoads.as_view()),


]
