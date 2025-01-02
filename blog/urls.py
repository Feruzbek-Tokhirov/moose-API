from django.urls import path
from .views import ContactCreateAPIView, AboutListAPIView, ArticleListAPIView, ArticleDetailAPIView

urlpatterns = [
    path("blog/contact/", ContactCreateAPIView.as_view()),
    path("blogs/<int:pk>/", ArticleDetailAPIView.as_view()),
    path("blog/about/", AboutListAPIView.as_view()),
    path("blogs/", ArticleListAPIView.as_view()),
]
