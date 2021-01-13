from django import forms

from .models import Article, Course


class CreateArticleForm(forms.ModelForm):
    title = forms.CharField(label='', widget=forms.TextInput(
        attrs={"placeholder": "Your title"}))
    content = forms.CharField(label='', widget=forms.Textarea(
        attrs={"rows": 20, "cols": 120, "placeholder": "Content of your article"}))
    active = forms.BooleanField(label='Active?', required=False)

    class Meta:
        model = Article
        fields = [
            'title',
            'content',
            'active',
        ]


class ArticleModelForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = [
            'title',
            'content',
            'active',
        ]


class CourseModelForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title']

    def clean_title(self):  # name is clean_<field name>
        title = self.cleaned_data.get('title')
        if title.lower() == 'abc':
            raise forms.ValidationError("this is not a valid title")
        return
