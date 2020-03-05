from django import forms
from .models import Post


class AddPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("caption", "image", "author")
        # fields = "__all__"
