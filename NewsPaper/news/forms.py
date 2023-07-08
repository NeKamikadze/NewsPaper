from django import forms
from django.shortcuts import redirect
from django.core.exceptions import ValidationError
from django.contrib.auth.decorators import login_required
from .models import Post, Category
from allauth.account.forms import SignupForm
from django.contrib.auth.models import Group


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


class BasicSignupForm(SignupForm):
    def save(self, request):
        user = super(BasicSignupForm, self).save(request)
        common_group = Group.objects.get(name='common')
        common_group.user_set.add(user)
        return user

