from django.core.cache import cache
from django.db import models
from django.contrib.auth.models import User
from django.db.models import *
from django.urls import reverse


class Author(models.Model):
    name = models.OneToOneField(User, on_delete=models.PROTECT)
    user_rating = models.IntegerField(default=0)

    def __str__(self):
        return self.name.username

    def update_rating(self):
        rating_post_author = Post.objects.filter(author=self).aggregate(Sum('post_rating'))['post_rating__sum'] * 3
        rating_comments_author = Comment.objects.filter(user=self.name).aggregate(Sum('comment_rating'))['comment_rating__sum']
        rating_comments_all_posts_author = Comment.objects.filter(post__author__name=self.name).aggregate(Sum('comment_rating'))['comment_rating__sum']

        self.user_rating = rating_post_author + rating_comments_author + rating_comments_all_posts_author
        self.save()


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    subscribers = models.ManyToManyField(User, blank=True)

    def __str__(self):
        return self.name


article = 'AR'
news = 'NE'

TYPES = [
    (article, 'Статья'),
    (news, 'Новость')
]


class Post(models.Model):
    create_time = models.DateTimeField(auto_now_add=True)
    type = models.CharField(max_length=2, choices=TYPES, default=news)
    title = models.CharField(max_length=255)
    content = models.TextField()
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

    def __str__(self):
        return f'{self.title.title()}: {self.content[:50]}'

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        cache.delete(f'post-{self.pk}')


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.PROTECT)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)


class Comment(models.Model):
    content = models.TextField()
    time_in = models.DateTimeField(auto_now_add=True)
    comment_rating = models.IntegerField(default=0)

    user = models.ForeignKey(User, on_delete=models.PROTECT)
    post = models.ForeignKey(Post, on_delete=models.PROTECT)

    def like(self):
        self.comment_rating += 1
        self.save()

    def dislike(self):
        self.comment_rating -= 1
        self.save()




