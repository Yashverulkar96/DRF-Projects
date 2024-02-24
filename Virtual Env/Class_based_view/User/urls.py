from . import views
from django.urls import path,include

urlpatterns = [
   path('user/',views.User.as_view()),
   path('user/<int:pk>/',views.User_details.as_view()),
]