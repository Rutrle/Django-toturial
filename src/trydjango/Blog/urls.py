from django.urls import path, include
from .views import create_article, article_list_view, article_detail_view, ArticleListView, ArticleDetailView, ArticleCreateView, ArticleUpdateView

app_name = 'Blog'
urlpatterns = [
    path('', create_article),
    path('articles', article_list_view),
    path('articles/<int:my_id>/', article_detail_view),

    path('articleclass', ArticleListView.as_view(), name='ArticleListView'),
    path('articleclass/<int:id>/', ArticleDetailView.as_view(),
         name='ArticleDetailView'),  # pk is default argument here standing for primary key => previously instead of id
    path('articleclass/create/', ArticleCreateView.as_view(),
         name='ArticleCreatetView'),
    path('articleclass/<int:id>/update/',
         ArticleUpdateView.as_view(), name='article-update'),
]
