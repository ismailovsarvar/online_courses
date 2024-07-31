from django import forms
from blogs.models import Comment


class CommentModelForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ()