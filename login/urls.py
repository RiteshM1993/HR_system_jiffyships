from django.conf.urls import url
from login import views

urlpatterns = [
    url(r'^$', views.loginView.as_view()),
    url(r'^dashboard/$', views.dashboardView.as_view()),

]