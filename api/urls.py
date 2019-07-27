from django.urls import path, include
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers



urlpatterns = [
    path('blog/', include('blog.urls')),
    path('question/', include('question.urls')),
    path('users/', include('users.urls')),
    path('a', FileUploadView.as_view()),

]







