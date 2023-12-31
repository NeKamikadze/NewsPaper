from django.urls import path
from .views import PostsList, PostDetail, SearchList, PostCreate, PostUpdate, PostDelete, CategoryPostList, upgrade_me,\
    subscribe
from django.views.decorators.cache import cache_page


urlpatterns = [
    path('', cache_page(60)(PostsList.as_view()), name='post_list'),
    path('<int:pk>', cache_page(300)(PostDetail.as_view()), name='post_detail'),
    path('search/', SearchList.as_view(), name='search_list'),
    path('create/', PostCreate.as_view(), name='news_create'),
    path('<int:pk>/edit/', PostUpdate.as_view(), name='news_edit'),
    path('<int:pk>/delete/', PostDelete.as_view(), name='news_delete'),
    path('articles/create/', PostCreate.as_view(), name='article_create'),
    path('articles/<int:pk>/edit/', PostUpdate.as_view(), name='article_edit'),
    path('articles/<int:pk>/delete/', PostDelete.as_view(), name='article_delete'),
    path('upgrade/', upgrade_me, name='upgrade'),
    path('category/<int:pk>/', CategoryPostList.as_view(), name='category_news'),
    path('category/<int:pk>/subscribe/', subscribe, name='subscribe'),
 ]
