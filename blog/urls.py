from django.urls import path, include
from rest_framework import routers
from blog.views import *


router = routers.DefaultRouter()
router.register('comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # path('postings/<int:pk>', PostingDetailView.as_view()),


    path('postings/', post_list, name="post_list"),
    path('postings/<int:pk>', post_detail, name="post_detail"),
    path('postings/<int:pk>/comments', post_comments, name="post_comments")
]
