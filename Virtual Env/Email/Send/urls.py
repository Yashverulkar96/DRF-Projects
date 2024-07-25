from django.urls import path,include
from .views import *
urlpatterns = [
    path('api/send/mail',SendEmail.as_view()),
]