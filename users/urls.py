from django.urls import include, path
from .views import RegisterUserView, UserDetailView, CustomLogin, UserView, CustomLogout, login
from rest_framework import routers
from users import views as users_views

urlpatterns = [
    path('registration', RegisterUserView.as_view()),
    path('login', CustomLogin.as_view()),
    path('logout', CustomLogout.as_view()),
    path('users',UserView.as_view()),


    path('', include('rest_auth.urls')),
    path('<int:pk>', UserDetailView.as_view()),

]
#urlpatterns = format_suffix_patterns(urlpatterns)


