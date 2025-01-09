from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Contact, About, Article, Comment
from .serilazers import ContactSerializer, AboutSerializer, ArticleSerializer, CommentSerializer
from rest_framework.pagination import LimitOffsetPagination


# class BlogCursorPagination(CursorPagination):
#     page_size = 1  # Har bir sahifada ko'rsatiladigan elementlar soni
#     ordering = '-create_date'


class AboutListAPIView(generics.ListAPIView):
    queryset = About.objects.all()
    serializer_class = AboutSerializer


class ContactCreateAPIView(generics.CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class ArticleListAPIView(APIView):
    def get(self, request):
        category_id = request.query_params.get('category_id')
        tags = request.query_params.getlist('tags')
        articles = Article.objects.filter(is_published=True)
        if category_id:
            articles = articles.filter(category_id=category_id)
        if tags:
            articles = articles.filter(tags__title__in=tags).distinct()

        paginator = LimitOffsetPagination()
        paginator.default_limit = 10
        paginated_queryset = paginator.paginate_queryset(articles, request)
        if paginated_queryset is None:
            return Response({"detail": "No articles found"})

        serializer = ArticleSerializer(paginated_queryset, many=True)
        return paginator.get_paginated_response(serializer.data)


class ArticleDetailAPIView(APIView):
    def get(self, request, pk):
        article = Article.objects.get(id=pk)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)


class CommentAPIView(APIView):
    def post(self, request, pk):
        try:
            article = Article.objects.get(id=pk)
        except Article.DoesNotExist:
            return Response({"message": "Article does not exist"}, status=status.HTTP_404_NOT_FOUND)
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(article=article)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({"message": "Qandaydur xatolik mavjud", "error": serializer.errors},
                        status=status.HTTP_400_BAD_REQUEST)
