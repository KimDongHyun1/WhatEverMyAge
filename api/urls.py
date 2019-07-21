from django.urls import path, include
from users.views import CustomListView

urlpatterns = [
    path('blog/', include('blog.urls')),
    path('question/', include('question.urls')),
    

    path('users/', include('users.urls')),
    path('', include('rest_auth.urls')),        
    path('registration/', include('rest_auth.registration.urls')),
    path('registration/<int:pk>/', CustomListView.as_view()),
]