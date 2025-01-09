from rest_framework import serializers

from .models import Contact, About, Article, Comment, Category, Tag


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'


class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["id", 'full_name', 'description', 'create_date', 'update_date']
        read_only_fields = ['create_date', 'update_date']


class ArticleSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    category = CategorySerializer(read_only=True)
    tags = TagSerializer(many=True, read_only=True)

    class Meta:
        model = Article
        fields = ["id", "title", "author", 'category', 'image', 'description', 'how_work', 'tags', 'create_date',
                  'update_date',
                  'is_published', "comments"]
        read_only_fields = ['create_date', 'update_date']
