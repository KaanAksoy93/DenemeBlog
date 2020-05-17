from django import forms
from .models import Post
from captcha.fields import ReCaptchaField


class PostForm(forms.ModelForm):
    captcha = ReCaptchaField()
    class Meta:

        model = Post
        fields = [
            'title',
            'content',

        ]