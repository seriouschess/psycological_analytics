from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^disclaimer$', views.disclaimer),
    url(r'^new/a$', views.newSurveyA),
    url(r'^new/b$', views.newSurveyB),
    url(r'^summary/(?P<user_id>\d+)$', views.user_summary), #one user's data
    url(r'^summary$', views.dataSummary), #all data
    url(r'^summary/analytics$', views.analytics) #correlation graphs
]
