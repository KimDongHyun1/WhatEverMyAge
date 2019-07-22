from django.urls import path, include



urlpatterns = [
    path('blog/', include('blog.urls')),
    path('question/', include('question.urls')),
    path('', include('users.urls')),
]


