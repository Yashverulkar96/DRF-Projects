from django.urls import path
from . import views

urlpatterns = [
    path('user/', views.user),
    path('user/<int:pk>/',views.user_details),

    # -------------------------------------------------------
    # path('user/', views.user),
    # path('user/create/',views.create_user),
    # path('user/<int:pk>/',views.user_details),
]