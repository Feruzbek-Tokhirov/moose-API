from .models import Contact, About, Article, Comment
from rest_framework.views import APIView
from rest_framework import generics, status
from .serializer import ContactSerializer, AboutSerializer, ArticleSerializer
from rest_framework.response import Response


class AboutListAPIView(generics.ListAPIView):
    queryset = About.objects.all()
    serializer_class = AboutSerializer


class ContactCreateAPIView(generics.CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class ArticleListAPIView(APIView):
    def get(self, request):
        articles = Article.objects.filter(is_published=True)
        serializer = ArticleSerializer(articles, many=True)
        data = {
            "Artiklar royxati": serializer.data
        }
        return Response(data, status=status.HTTP_200_OK)


class ArticleDetailAPIView(APIView):
    def get(self, request, pk):
        article = Article.objects.get(id=pk)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
