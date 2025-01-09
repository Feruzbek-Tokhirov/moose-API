from django.urls import path
from .views import ContactCreateAPIView, AboutListAPIView, ArticleListAPIView, ArticleDetailAPIView, CommentAPIView

urlpatterns = [
    path('blogs/', ArticleListAPIView.as_view()),
    path('blogs/<int:pk>/', ArticleDetailAPIView.as_view()),
    path('blogs/<int:pk>/comment/', CommentAPIView.as_view()),
    path('blog/contact/', ContactCreateAPIView.as_view()),
    path('blog/about/', AboutListAPIView.as_view()),
]
