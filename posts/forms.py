from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):
    # title = forms.CharField(
    #     label='제목',
    #     widget=forms.TextInput(
    #         attrs={'class': 'form-control'}
    #     )
    # )
    class Meta:
        model = Post
        fields = '__all__'


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        # fields = '__all__'
        # fields => 추가할 필드 이름 목록
        fields = ('content',)
        # exclude => 제외할 필드 이름 목록
        # exclude = ('post',)