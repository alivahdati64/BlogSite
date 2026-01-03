from django.urls import path
from blog.views import *
from blog.feeds import LatestEntriesFeed

app_name='blog'  #url

urlpatterns = [
    # path('home',index_view),
    path('', blog_view, name='index'),
    # path('single', blog_single, name='single'),
    path('<int:pid>', blog_single, name='single'),
    # path('category/<str:cat_name>', blog_category, name='category'),
    path('category/<str:cat_name>', blog_view, name='category'),
    path('tag/<str:tag_name>', blog_view, name='tag'),
    path('author/<str:author_username>', blog_view, name='author'),
    path('search/', blog_search, name='search'),
    path("rss/feed/", LatestEntriesFeed()),
    path('test', test, name='test'),
    # path('<str:name>/family/<str:family>/age/<int:age>', test2, name='test2')
     path('post-<int:pid>', test2, name='test2')
]