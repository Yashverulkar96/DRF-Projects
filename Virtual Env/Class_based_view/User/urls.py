from . import views
from django.urls import path,include

urlpatterns = [
   path('',views.User.as_view()),
   path('<int:pk>/',views.User_details.as_view()),
]