from django import forms
from .models import BlogPost


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'slug', 'comparison_keyword', 'content', 'published']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'e.g., Grok vs ChatGPT: What Developers Actually Say in 2026'
            }),
            'slug': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'e.g., grok-vs-chatgpt'
            }),
            'comparison_keyword': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'e.g., Grok vs ChatGPT'
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-textarea',
                'placeholder': 'Paste HTML content here',
                'rows': 20
            }),
            'published': forms.CheckboxInput(attrs={
                'class': 'form-checkbox'
            })
        }
