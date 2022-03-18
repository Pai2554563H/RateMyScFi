from django import forms
from forum.models import Post, PostReply


class PostForm(forms.ModelForm):
    # author = forms.
    title = forms.CharField(widget=forms.Textarea, help_text="Enter the title.")
    content = forms.CharField(widget=forms.Textarea, help_text="Enter the your post text.")

    class Meta:
        model = Post
        fields = ('title', 'content')


class ReplyForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea, help_text="Enter the your reply.")

    class Meta:
        model = PostReply
        fields = ('content',)
        exclude = ('post',)
