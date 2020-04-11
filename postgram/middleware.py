"""
Platzigram middleware cataog.
Los middlewares se ejecutan antes de la vista de request y antes de la vista del response.
"""

#Django
from django.shortcuts import redirect
from django.urls import reverse


#Clase no recibe nada, ver docuemntacion de Middleware
class ProfileCompletionMiddleware:
    """
    Profile completion middleware.

    Ensure every user that is interacting with the platforn
    have their profile picture and biography.
    """
    def __init__(self, get_respose):
        self.get_response = get_respose #No hace nada con el response, simplemente lo trae.

    #Aqui va la lógica
    def __call__(self, request):
        """
        Code to be executed for each request before the view is called.
        """

        if not request.user.is_anonymous:

            #Para que al entrar a /admin/ el middleware si nos permita.
            if not request.user.is_staff:
                profile = request.user.profile
                
                #Accion a realizar si no tiene foto de perfil o biografía
                if not profile.picture or not profile.biography:
                    
                    #El primero se hace para que no nos de un bucle infinito de update_profile y el segundo para poder deslogearse.
                    if request.path not in [reverse('users:update'), reverse('users:logout')]: #reverse('update_profile') == '/users/me/profile'
                        return redirect('users:update') #redirecciona al path con nombre 'update_profile'

        #Si tiene profile pic y biografía, pues entonces no hace nada y devuelve el response normal.
        response = self.get_response(request)
        return(response)