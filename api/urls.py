from django.urls import path, include
from . import views
urlpatterns = [
    path('rider/', views.RiderAPI.as_view()),
    path('requester/', views.RequesterAPI.as_view()),
    path('my-requests/', views.UserRequestorList.as_view()),
    path('user-requests-matched/', views.UserRequestMatchListAPI.as_view()),
    path('user-request-update/<int:pk>/', views.UserRequesterUpdate.as_view())
]