from django.urls import path, include
from rest_framework import routers
from blog import views as blog_views #from board.views import PostingViewSet, CommentViewSet

router=routers.DefaultRouter()
router.register('blog', blog_views.BlogViewSet)
router.register('comment', blog_views.CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    #path('blogs/<int:pk>/', blog_views.blog_detail),
    path('blog/<int:pk>/comment/', blog_views.blog_comment), 
]   