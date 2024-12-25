from django.views.generic import ListView , DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import TemplateView
from .models import Article

###
from django.shortcuts import render, redirect


class LandingPageView(TemplateView):
    
    template_name = "landing_page.html"

def Landingpagefunc(request):
    author =""
    print(request.user)
    if request.user.is_authenticated:
        author = request.user
        
    return render(request, 'landing_page.html', {'username': author})
###########2
def article_list_view(request):
    articles = Article.all()
    
    return render(request, 'article_list.html', {'articles': articles})

class AllArticleListView(ListView):
    model = Article
    template_name = "article_list.html"

class ArticleListView(ListView):
    model = Article
    template_name = "my_article_list.html"
    
    def get_queryset(self):
        return Article.objects.for_user(self.request.user)

class ArticleDetailView(LoginRequiredMixin, DetailView):
    model = Article
    template_name = "article_detail.html"

class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin ,UpdateView): 
    model = Article
    fields = (
    "title",
    "body",
    )

    template_name = "article_edit.html"
    def test_func(self): 
        obj = self.get_object()
        return obj.author == self.request.user

class ArticleDeleteView(LoginRequiredMixin,UserPassesTestMixin, DeleteView): 
    model = Article
    template_name = "article_delete.html"
    success_url = reverse_lazy("article_list")

    def test_func(self): 
        obj = self.get_object()
        return obj.author == self.request.user

class ArticleCreateView(LoginRequiredMixin, CreateView): 
    model = Article
    template_name = "article_new.html"
    fields = (
    "title",
    "body",
)
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    
  