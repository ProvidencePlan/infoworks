from django.conf.urls import url
from front_page import views

urlpatterns = [
    url(r'^search$', views.search, name="search_page"),
    url(r'^search/schools-and-districts', views.landing_page, name="landing_page"),
    url(r'^school/(?P<slug>[\w-]+)$', views.school, name="school"),
    url(r'^district/(?P<slug>[\w-]+)$', views.district, name="district"),
    url(r'^state$', views.state, name="state"),
    url(r'^state/(?P<slug>[\w-]+)$', views.states, name="states"),
    url(r'^understanding-data/dictionary$',views.dictionary,name="dictionary"),
    ]

