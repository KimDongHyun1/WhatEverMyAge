from django.urls import path, include
from rest_framework import routers
from blog.views import *


router = routers.DefaultRouter()
router.register('comments', CommentViewSet)



urlpatterns = [
    path('', include(router.urls)),
    path('postings/', posting_list, name='posting_list'),
    path('postings/<int:pk>', posting_detail),
    path('postings/<int:pk>/comments', post_comments, name="post_comments"),
    path('likeplus/<int:pk>', likeplus, name='likeplus'),
]
