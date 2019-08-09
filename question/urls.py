from django.urls import path, include
from rest_framework import routers
from . import views


router=routers.DefaultRouter()
router.register('questions', views.QuestionViewSet)
router.register('q_comments', views.Q_CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('questions/<int:pk>', views.question_detail),
    path('questions/<int:pk>/q_comments', views.question_q_comment), 
]



