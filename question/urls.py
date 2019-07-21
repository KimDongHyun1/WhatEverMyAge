from django.urls import path, include
from rest_framework import routers
from . import views


router=routers.DefaultRouter()
router.register('question', views.QuestionViewSet)
router.register('q_comment', views.Q_CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('questions/<int:pk>/', views.question_detail),
    path('question/<int:pk>/q_comment/', views.question_q_comment), 
]



