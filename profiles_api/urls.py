from django.urls import path
from profiles_api.views import HelloUserApi

urlpatterns = [
    path('hello-api/', HelloUserApi.as_view()),
]