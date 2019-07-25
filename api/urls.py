from django.urls import path, include
from .views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('blog/', include('blog.urls')),
    path('question/', include('question.urls')),
    path('', include('users.urls')),
    path('hello/', FileUploadView.as_view()),
]


if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
