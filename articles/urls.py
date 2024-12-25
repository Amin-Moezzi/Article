from django.urls import path
from .views import ArticleListView, ArticleDetailView, ArticleUpdateView, ArticleDeleteView, ArticleCreateView, AllArticleListView, LandingPageView
from .views import Landingpagefunc, article_list_view
urlpatterns = [
path("list", AllArticleListView.as_view(), name="article_list"),
path("My_articles", ArticleListView.as_view(), name="user_article_list"),
path("<int:pk>/", ArticleDetailView.as_view(),name="article_detail"), 
path("<int:pk>/edit/", ArticleUpdateView.as_view(), name="article_edit"), 
path("<int:pk>/delete/", ArticleDeleteView.as_view(), name="article_delete"),
path("new/", ArticleCreateView.as_view(), name="article_new"),
path('', Landingpagefunc, name='landing_page'),
]