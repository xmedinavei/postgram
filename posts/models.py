"""Posts models."""

#Django
from django.db import models
from django.contrib.auth.models import User


#Este se conecta con el formulario PostForm de form.py
class Post(models.Model):
    """Post model."""

    #Para relacionarlo con nuestro usuario
    #USANDO FOREIGN KEY
    #documentation Django Model Field Reference
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey('users.Profile', on_delete=models.CASCADE) #'users.Profile' = app.cosa_que_desea_importar

    title = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='posts/photos')

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return title and username."""
        return '{} by @{}'.format(self.title, self.user.username)

