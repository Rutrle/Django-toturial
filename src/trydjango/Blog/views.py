from django.shortcuts import render, get_object_or_404
from .forms import CreateArticleForm, ArticleModelForm
from .models import Article
from django.views.generic import(
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView
)
# Create your views here.


def create_article(request):
    form = CreateArticleForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = CreateArticleForm()

    context = {
        'form': form
    }
    return render(request, "Article_create.html", context)


def article_list_view(request):
    queryset = Article.objects.all()  # list of objects
    context = {
        "object_list": queryset
    }
    return render(request, "Article_list.html", context)


def article_detail_view(request, my_id):
    obj = Article.objects.get(id=my_id)

    context = {
        'object': obj
    }
    return render(request, "Article_detail.html", context)


# same function as article_list_view
class ArticleListView(ListView):

    template_name = 'article_class_list.html'  # overrides generic template address

    # going to loo automatically for <blog>/<modelname>_list.html
    queryset = Article.objects.all()


class ArticleDetailView(DetailView):

    # overrides generic template address
    template_name = 'article_class_detail.html'

    queryset = Article.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article, id=id_)


class ArticleCreateView(CreateView):

    # overrides generic template address
    template_name = 'article_class_create.html'
    form_class = ArticleModelForm
    success_url = '/'  # overiding where the django will take me afterwards

    # going to loo automatically for <blog>/<modelname>_list.html
    queryset = Article.objects.all()

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)


class ArticleUpdateView(UpdateView):
    # overrides generic template address
    template_name = 'article_class_create.html'
    form_class = ArticleModelForm
    success_url = '/'  # overiding where the django will take me afterwards

    # going to loo automatically for <blog>/<modelname>_list.html
    queryset = Article.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article, id=id_)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)


class ArticleDeleteView(DeleteView):

    # overrides generic template address
    template_name = 'article_class_delete.html'

    queryset = Article.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article, id=id_)
