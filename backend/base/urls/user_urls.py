from django.urls import path
from base.views import user_views as views


urlpatterns = [
    path('login/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    # register / create new user
    path('register/', views.registerUser, name='register'),
    # get all the users from the db => just for admins 
    path('', views.getUsers, name='users'),
    # user profiles
    path('profile/', views.getUserProfile, name='users-profile'),
]