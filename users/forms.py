"""User forms."""

#Django
from django import forms

#Models
from django.contrib.auth.models import User
from users.models import Profile

class SignupForm(forms.Form):
    """Sign up form."""

    username = forms.CharField(min_length=4, max_length=50, widget=forms.TextInput(attrs={"class": "form-control"}))
    password = forms.CharField(max_length=70, widget=forms.PasswordInput(attrs={"class": "form-control"}))
    password_confirmation = forms.CharField(max_length=70, widget=forms.PasswordInput(attrs={"class": "form-control"}))
    first_name = forms.CharField(min_length=2, max_length=50, widget=forms.TextInput(attrs={"class": "form-control"}))
    last_name = forms.CharField(min_length=2, max_length=50, widget=forms.TextInput(attrs={"class": "form-control"}))

    email = forms.CharField(
        min_length=6,
        max_length=70,
        widget=forms.EmailInput(attrs={"class": "form-control"})
    )

    def clean_username(self):
        """Username must be unique."""
        username = self.cleaned_data['username']
        username_taken = User.objects.filter(username=username).exists()
        
        if username_taken:
            raise forms.ValidationError('Username is already in use.')

        return username


    def clean(self):
        """Verify password confirmation match."""
        data = super().clean() 

        password = data['password']
        password_confirmation = data['password_confirmation']

        if password != password_confirmation:
            raise forms.ValidationError('Passwords do not match.')
        
        return data

    def save(self):
        """Create User and profile."""
        data = self.cleaned_data #Donde están los datos del formulario
        data.pop('password_confirmation') #Eliminar ese dato que no sirve para crear el ususario

        user = User.objects.create_user(**data) #**data enivarle todo el diccionatio en lugar de (email=data['email'], etc)
        profile = Profile(user=user)
        profile.save()


#Reemplazado en views.py por el UpdateView en class UpdateProfile

#class ProfileForm(forms.Form):
#    """Profile forms."""
#
#    website = forms.URLField(max_length=200, required=True)
#    biography = forms.CharField(max_length=500, required=False)
#    phone_number = forms.CharField(max_length=20, required=False)
#    picture = forms.ImageField()