from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'author', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}), 
            'title_tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tag'}),  
            'author': forms.Select(attrs={'class': 'form-control'}),  
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter Your Post Here!'}),   
        }


class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}), 
            'title_tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tag'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter Your Post Here!'}), 
        }