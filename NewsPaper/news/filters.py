from django_filters import FilterSet, DateFilter, CharFilter, ModelChoiceFilter
from .forms import *
from .models import Post, Author, Category


class PostFilter(FilterSet):
    category = ModelChoiceFilter(field_name='category', queryset=Category.objects.all(), label='Категория:',
                                 empty_label='Любая')
    title = CharFilter(field_name='title', lookup_expr='icontains', label='Название публикации:')
    author = ModelChoiceFilter(field_name='author', queryset=Author.objects.all(), label='Автор публикации:')
    create_time = DateFilter(field_name='create_time', lookup_expr='gt', label='Опубликовано позже:', widget=forms.
                             DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Post
        fields = {
            'category': ['exact'],
            'author': ['exact'],
        }
