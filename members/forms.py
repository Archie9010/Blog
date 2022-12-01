from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django import forms
from blog.models import Profile


class ProfilePageForm(forms.ModelForm):
    """Model form for users to edit user's profile details"""
    class Meta:
        model = Profile
        fields = ('profile_pic', 'facebook_url', 'instagram_url', 'youtube_url', 'twitter_url', 'bio')

        widgets = {
            'facebook_url': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Please Enter Full URL e.g. www.site.com/handle'}),
            'instagram_url': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Please Enter Full URL e.g. www.site.com/handle'}),
            'youtube_url': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Please Enter Full URL e.g. www.site.com/handle'}),
            'twitter_url': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Please Enter Full URL e.g. www.site.com/handle'}),
            'Bio': forms.Textarea(attrs={'class': 'form-control'}),
            }


class SignUpForm(UserCreationForm):
    """Creation user form for users to sign up"""
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'


class EditProfileForm(UserChangeForm):
    """User change form for users to edit user's personal details"""
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}))
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email',)

    
class PasswordChangingForm(PasswordChangeForm):
    """Password change form for users to change user's password"""
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Old Password', 'type':'password'}))
    new_password1 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'New Paasword', 'type':'password'}))
    new_password2 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Re-Enter New Password', 'type':'password'}))

    class Meta:
        model = User
        fields = ('old_password', 'password1', 'password2')