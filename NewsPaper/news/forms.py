from django import forms
from django.core.exceptions import ValidationError
from .models import Post, Category


class PostForm(forms.ModelForm):
    title = forms.CharField(max_length=50)

    class Meta:
        model = Post
        fields = ['category', 'title', 'content', 'author']

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get("title")
        content = cleaned_data.get("content")

        if title == content:
            raise ValidationError(
              "Текст публикации не должен совпадать с названием."
            )

        return cleaned_data
