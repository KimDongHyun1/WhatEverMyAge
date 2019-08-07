from django.urls import path, include
from rest_framework import routers
from blog.views import CommentViewSet, LoveViewSet, PostingList, PostingDetail, post_comments


router = routers.DefaultRouter()
router.register('comments', CommentViewSet)
router.register('loves', LoveViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('postings/', PostingList.as_view()),
    path('postings/<int:pk>', PostingDetail.as_view()),
    path('postings/<int:pk>/comments', post_comments, name="post_comments"),
    #path('aaa/<int:pk>', post_list, name='post_list'),
]
