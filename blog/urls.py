from django.urls import path, include
from rest_framework import routers
from blog.views import *


# router = routers.DefaultRouter()
# router.register('postings', PostingViewSet)
# router.register('comments', CommentViewSet)

urlpatterns = [
    # path('', include(router.urls)),
    # path('postings/<int:pk>', posting_detail, name="posting_detail"),
    # path('postings/<int:pk>/comments', posting_comments),

    path('postings/', post_list, name="post_list"),
]
