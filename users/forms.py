"""User forms."""

#Django
from django import forms

#Models
from django.contrib.auth.models import User
from users.models import Profile

class SignupForm(forms.Form):
    """Sign up form."""

    username = forms.CharField(min_length=4, max_length=50)

    #Widget, ver documentación.
    #Widget sirven para hacer pequeñas validaciones de HTML sin mostrar el input.
    password = forms.CharField(
        max_length=70, 
        widget=forms.PasswordInput()
    )
    password_confirmation = forms.CharField(
        max_length=70,
        widget=forms.PasswordInput()
    )

    first_name = forms.CharField(min_length=2, max_length=50)
    last_name = forms.CharField(min_length=2, max_length=50)

    #Widget de validación de email. Ver doc de widgets
    email = forms.CharField(
        min_length=6,
        max_length=70,
        widget=forms.EmailInput()
    )


    #Ver documentacion Forms and Field validation
    # clean_<campo a validar> sirve para validar un campo. Ver documentacion
    def clean_username(self):
        """Username must be unique."""
        username = self.cleaned_data['username'] #Donde están los datos del formulario
        
        #Querie a la base de datos.
        #Se usa .filter en lugar de .GET debido a que .GET fallaría su el ususario no existe.
        username_taken = User.objects.filter(username=username).exists() #.exists() regresa un booleano True o False si existe el ususario
        
        if username_taken:
            raise forms.ValidationError('Username is already in use.') #Manda el error hasta el HTML.
        
        return username #Cuando se hace la validación de un campo, se tiene que regresar un campo.


    #Validación final
    #Validar password. Validar campos que dependen de otros. Ver documentación de Forms and Field Validation
    def clean(self):
        """Verify password confirmation match."""
        data = super().clean() #Traer a clean antes de ser sobreescrito por este codigo.

        password = data['password']
        password_confirmation = data['password_confirmation']

        if password != password_confirmation:
            raise forms.ValidationError('Passwords do not match.') #Lanza el error hacia el HTML directamente.
        
        return data #Cuando se hace la validación de un campo, se tiene que regresar un campo.


    #Como estamos guardando los datos del formulario
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