from django.urls import path, include
from .views import create_article, article_list_view, article_detail_view, ArticleListView

app_name = 'Blog'
urlpatterns = [
    path('', create_article),
    path('articles', article_list_view),
    path('articles/<int:my_id>/', article_detail_view),

    path('articlelist', ArticleListView.as_view(), name='ArticleListView')
]
