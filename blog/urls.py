from django.urls import path, include
from rest_framework import routers
from blog.views import *
#from blog.views import CommentViewSet, PostingList, posting_detail, post_comments, like_list, like_detail


router = routers.DefaultRouter()
router.register('comments', CommentViewSet)



urlpatterns = [
    path('', include(router.urls)),
    path('postings/', posting_list, name='posting_list'),#PostingList.as_view()),
    path('postings/<int:pk>', posting_detail),
    path('postings/<int:pk>/comments', post_comments, name="post_comments"),
    path('like_list/', like_list, name="like_list"),
    path('like_detail/<int:pk>', like_detail, name='like_detail'),
    path('likeplus/<int:pk>', likeplus, name='likeplus'),
]
