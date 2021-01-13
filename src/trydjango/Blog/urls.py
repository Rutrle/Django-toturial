from django.urls import path, include
from .views import (create_article,
                    article_list_view,
                    article_detail_view,
                    ArticleListView,
                    ArticleDetailView,
                    ArticleCreateView,
                    ArticleUpdateView,
                    my_fbv,
                    ArticleDeleteView,
                    CourseView
                    )

app_name = 'blog'
urlpatterns = [
    path('', create_article),
    path('articles', article_list_view),
    path('articles/<int:my_id>/', article_detail_view),

    path('articleclass/', ArticleListView.as_view(), name='ArticleListView'),
    path('articleclass/<int:id>/', ArticleDetailView.as_view(),
         name='ArticleDetailView'),  # pk is default argument here standing for primary key => previously instead of id
    path('articleclass/create/', ArticleCreateView.as_view(),
         name='ArticleCreatetView'),
    path('articleclass/<int:id>/update/',
         ArticleUpdateView.as_view(), name='article-update'),
    path('articleclass/<int:id>/delete/',
         ArticleDeleteView.as_view(), name='article-delete'),
    # path('about/',
    #    my_fbv, name='article-delete'),
    path('courses/',
         CourseView.as_view(template_name='about.html'), name='article-delete'),
    path('courses/<int:id>/',
         CourseView.as_view(template_name="course_detail.html"), name='article-delete'),
]
