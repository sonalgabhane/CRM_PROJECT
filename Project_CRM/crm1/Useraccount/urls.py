
from django.urls import path
from .views import *


path("signup/",RegisterView.as_view(),name="signup"),
path("login/",LoginView.as_view(),name="login"),
path('logout/<int:pk>/delete/', UserDeleteView.as_view(), name='my_logout'),


######################################## Facebook Ads ###########################################


from django.urls import re_path, path, include
from .views import FacebookWebhook

path("webhook-facebook/", FacebookWebhook.as_view(), name="facebook-webhook"),