from django.shortcuts import render
from .forms import CreateArticleForm
from .models import Article
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
