"""Post forms."""

#Django
from django import forms

#Models
from posts.models import Post


class PostForm(forms.ModelForm):
    """Post model form."""

    #Clase meta es la configuracion en general
    class Meta:
        """Form settings."""

        model = Post
        fields = ('user', 'profile', 'title', 'photo')
