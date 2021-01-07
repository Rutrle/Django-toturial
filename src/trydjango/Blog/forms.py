from django import forms

from .models import Article


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
