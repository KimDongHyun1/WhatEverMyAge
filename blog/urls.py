from django.urls import path, include
from rest_framework import routers
from blog.views import *


router = routers.DefaultRouter()
router.register('comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('postings/', PostingList.as_view()),
    path('postings/<int:pk>', PostingDetail.as_view()),
    path('postings/<int:pk>/comments', post_comments, name="post_comments"),

]
