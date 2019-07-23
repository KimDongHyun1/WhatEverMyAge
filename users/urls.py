from django.urls import include, path
from .views import RegisterUserView, UserDetailView, CustomLogin, UserView, CustomLogout
from rest_framework import routers
from users import views as users_views


urlpatterns = [
    path('registration/', RegisterUserView.as_view()),
    #path('registration/<int:pk>'),
    #path('login/', CustomLogin.as_view()),
    path('', include('rest_auth.urls')),
    path('logout/', CustomLogout.as_view()),
    path('users/',UserView.as_view()),
    path('<int:pk>', UserDetailView.as_view()),
]


