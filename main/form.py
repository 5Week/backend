from django.forms import ModelForm
from django import forms
from .models import Board
from django_summernote.fields import SummernoteTextField
from django_summernote.widgets import SummernoteWidget


class PostForm(forms.ModelForm):

    title = forms.CharField(
        label='글 제목',
        widget=forms.TextInput(attrs={'placeholder': '게시글 제목'}),
        required=True,
    )

    content = SummernoteTextField()

    field_order = [
        'title',
        'content',
        'writer'
    ]

    class Meta:
        model = Board
        fields = ['title', 'content']
        widgets = {
            'content': SummernoteWidget(),
    }

    def clean(self):
        cleaned_data = super().clean()

        title = cleaned_data.get('title', '')
        content = cleaned_data.get('content', '')
        writer = cleaned_data.get('writer', '')

        if title == '':
            self.add_error('title', '글 제목을 입력하세요')
        elif content =='':
            self.add_error('title', '내용을 입력하세요')
        else:
            self.title = title
            self.content = content
            self.writer = writer