from django.db import models
from django.contrib.auth.models import User
from django.db.models import *


class Author(models.Model):
    name = models.OneToOneField(User, on_delete=models.PROTECT, verbose_name='Автор')
    user_rating = models.IntegerField(default=0)

    def update_rating(self):
        rating_post_author = Post.objects.filter(author=self).aggregate(Sum('post_rating'))['post_rating__sum'] * 3
        rating_comments_author = Comment.objects.filter(user=self.name).aggregate(Sum('comment_rating'))['comment_rating__sum']
        rating_comments_all_posts_author = Comment.objects.filter(post__author__name=self.name).aggregate(Sum('comment_rating'))['comment_rating__sum']

        self.user_rating = rating_post_author + rating_comments_author + rating_comments_all_posts_author
        self.save()


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name='Категория')


article = 'AR'
news = 'NE'

TYPES = [
    (article, 'Статья'),
    (news, 'Новость')
]


class Post(models.Model):
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания публикации')
    type = models.CharField(max_length=2, choices=TYPES, default=news, verbose_name='Вид публикации')
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Контент публикации')
    post_rating = models.IntegerField(default=0)

    author = models.ForeignKey(Author, on_delete=models.PROTECT)
    category = models.ManyToManyField(Category, through='PostCategory')

    def like(self):
        self.post_rating += 1
        self.save()

    def dislike(self):
        self.post_rating -= 1
        self.save()

    def preview(self):
        return self.content[:124] + '...'


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.PROTECT)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)


class Comment(models.Model):
    content = models.TextField(verbose_name='Контент комментария')
    time_in = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания комментария')
    comment_rating = models.IntegerField(default=0)

    user = models.ForeignKey(User, on_delete=models.PROTECT)
    post = models.ForeignKey(Post, on_delete=models.PROTECT)

    def like(self):
        self.comment_rating += 1
        self.save()

    def dislike(self):
        self.comment_rating -= 1
        self.save()


