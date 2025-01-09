from django.db import models


class Tag(models.Model):
    title = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Article(models.Model):
    title = models.CharField(max_length=202)
    author = models.CharField(max_length=202)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='articles')
    image = models.ImageField(upload_to='article/')
    description = models.TextField()
    how_work = models.TextField(blank=True, null=True)
    tags = models.ManyToManyField(Tag, related_name='articles_tag')
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    full_name = models.CharField(max_length=202)
    description = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name


class About(models.Model):
    full_name = models.CharField(max_length=202)
    image = models.ImageField(upload_to='about/')
    body = models.CharField(max_length=200)
    description = models.TextField()
    how_i_work = models.TextField()

    def __str__(self):
        return self.full_name


class Contact(models.Model):
    full_name = models.CharField(max_length=202)
    email = models.EmailField()
    subject = models.CharField(max_length=202)
    message = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.full_name
