from django.urls import include, path
# from rest_framework import routers
from devopsup.views import *

urlpatterns = [
    path('instructions/', instructions, ),]