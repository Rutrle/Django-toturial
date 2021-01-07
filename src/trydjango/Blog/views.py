from django.shortcuts import render
from .forms import CreateArticleForm
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
