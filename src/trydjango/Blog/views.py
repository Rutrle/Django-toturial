from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import View
from .forms import CreateArticleForm, ArticleModelForm, CourseModelForm
from .models import Article, Course
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
    # overiding where the django will take me afterwards, reasonw are too many apps
    success_url = 'http://127.0.0.1:8000/blog/articleclass/'

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article, id=id_)

    def get_success_url(self):
        return reverse('blog:ArticleListView')


def my_fbv(request, *args, **kwargs):  # basic class
    return render(request, 'about.html', {})


class CourseView(View):
    template_name = "course_detail.html"

    def get(self, request, id=None, *args,  **kwargs):
        context = {}
        if id is not None:
            obj = get_object_or_404(Course, id=id)
            context['object'] = obj

        return render(request, self.template_name, context)


class CourseListView(View):
    template_name = "course_list.html"
    queryset = Course.objects.all()

    def get_queryset(self):
        return self.queryset

    def get(self, request, *args, **kwargs):
        context = {'object_list': self.get_queryset()}
        return render(request, self.template_name, context)


class CourseCreateView(View):
    template_name = "course_create.html"

    def get(self, request, *args,  **kwargs):
        form = CourseModelForm()
        context = {"form": form}

        return render(request, self.template_name, context)

    # post method

    def post(self, request, *args,  **kwargs):

        form = CourseModelForm(request.POST)
        if form.is_valid():
            form.save()
            form = CourseModelForm()

        context = {"form": form}

        return render(request, self.template_name, context)
