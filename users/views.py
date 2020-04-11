"""User views."""

#Django
#from django.shortcuts import render, redirect #metodo para renderizar y redireccinar url
#from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import views as auth_views
#from django.views.generic import TemplateView #Ver doc Class-based Views
from django.views.generic import DetailView, FormView, UpdateView #Ver doc Class-based Views
from django.urls import reverse, reverse_lazy

#Models
from django.contrib.auth.models import User
from posts.models import Post
from users.models import Profile

#Forms
from users.forms import  SignupForm #, ProfileForm

#Exceptions
#from django.db.utils import IntegrityError


#Para que muestre el detaill del usuario
#Ver url.py de Users
class UserDetailView(LoginRequiredMixin, DetailView): #Cambiamos TemplateView por DetailView. Ver doc.
    """User detail view of a specific username."""

    template_name = 'users/detail.html'
    slug_field = 'username'
    slug_url_kwarg = 'username' #url.py (users) <str:username>
    queryset = User.objects.all()
    context_object_bname = 'user'

    #Ya es un método predefinido, pero lo editaremos para meter posts.
    #ver ccbs.co.uk en DetailView
    def get_context_data(self, **kwargs):
        """Add user's posts to context."""
        context = super().get_context_data(**kwargs)
        user = self.get_object() #get_object() have el query de todos los usuarios
        context["posts"] = Post.objects.filter(user=user).order_by('-created') #muestra los posts del usuario.
        return context
    
#Ver ccbv.co.uk para mas clased-based views
class SignupView(FormView):
    """Users sign up view."""

    template_name = 'users/signup.html'
    form_class = SignupForm
    success_url = reverse_lazy('users:login')

    #ver doc de FormView.
    #Sobreescribimos el form_valid para que guarde los datos
    def form_valid(self, form):
        """Save form data."""
        form.save()
        return super().form_valid(form)


#Ver ccbv.co.uk para mas clased-based views
class UpdateProfileView(LoginRequiredMixin, UpdateView):
    """Update profile view."""

    template_name = 'users/update_profile.html'
    model = Profile
    fields = ['website', 'biography', 'phone_number', 'picture']

    #sobre escribimos el método para ue traiga el perfil del usuario. Ver ccbv.co.uk
    def get_object(self):
        """Return users's profile."""
        return self.request.user.profile
    
     #sobre escribimos el método para que redirija correctamente. Ver ccbv.co.uk
    def get_success_url(self):
        """Return to user's profile."""
        username = self.object.user.username
        return reverse('users:detail', kwargs={'username':username}) #get_success_url retorna un pk a la url.
                                                                    #nuestra url no usa pk. Por lo tanto usamos reverse...
                                                                    # para redirigir al detalle del perfil.
#Ver documentacion de Auth para mas información.
class LoginView(auth_views.LoginView):
    """Login view."""
    template_name = 'users/login.html'

class LogoutView(LoginRequiredMixin, auth_views.LogoutView):
    """Logout view."""
    template_name = 'users/logged_out.html'


#######################
####Codigo viejo #####
######################

###################
   # CON FORMS
###################
#usar debugger apra ver que hay dentro y que trae. En este caso request.method = POST y request.POST es un dictionary con datos del formulario.
#def signup(request):
#    """Sign up view."""
#
#    if request.method == 'POST':
#        form = SignupForm(request.POST) #no le enviamos request.FILES porque no requerimos ningun archivo0
#
#        if form.is_valid():
#            form.save()
#            return redirect('users:login')#
#
#    else:
#        form = SignupForm()
#
#    return render(
#        request=request,
#        template_name='users/signup.html',
#        context={'form':form},
#    )
################################################################################################################

        #############################################
        ###CODIGO VIEJO, SIN FORMULARIOS NI FORMS.PY#
        ##############################################
    #if request.method == 'POST':
    #    """Crear el usuario usando el formulario de envío. Luego el perfil."""

        #username = request.POST['username']
        #passwd = request.POST['passwd']
        #passwd_confirmation = request.POST['passwd_confirmation']

        #if passwd != passwd_confirmation:
        #    return render(request, 'users/signup.html', {'error':'Password confirmation does not match'})
        
        #Crear el usuario
        #Esto se encuentra en la documentacion de autenticacion de django

        #se parcha este error que sale en consola cuando se hace signup a un username que ya existe en la base de datos.
        #try:
        #    user = User.objects.create_user(username=username, password=passwd)
        #except IntegrityError: #este error se muestra en al consola cuando hace signup a un username ue ya existe.
        #    return render(request, 'users/signup.html', {'error':'Username is already in use.'})

        #user.first_name = request.POST['first_name']
        #user.last_name = request.POST['last_name']
        #user.email = request.POST['email']
        #user.save()

        #Crear ahora el perfil
        #profile = Profile(user=user)
        #profile.save()

        #return redirect('login')       
        
    #return render(request, 'users/signup.html')
###############################################################

################################################################
#@login_required
#def update_profile(request):
#    """Update users profile view."""
#    profile = request.user.profile
#
#    if request.method == 'POST':
#        form = ProfileForm(request.POST, request.FILES) #los archivos vienen desde request.FILES
#        if form.is_valid(): #Corre todas las validaciones (Valida el formulario, ver doc de working with forms)
#            data = form.cleaned_data#
#
#            profile.website = data['website']
#            profile.phone_number = data['phone_number']
#            profile.biography = data['biography']
#            profile.picture = data['picture']
#            profile.save()
#
#            url = reverse('users:detail', kwargs={'username':request.user.username})#
#
#            #Nos ayudamos de REVERSE para redirigir la url
#            return redirect(url) #Redireccionamos a detail y el enviamos el argumento necesario tambien.
#        
#    else:
#        form = ProfileForm()    
#
#    return render(
#        request = request,
#        template_name = 'users/update_profile.html',
#        context = {
#            'profile': profile,
#            'user': request.user,
#            'form': form,
#            }
#        )

###############################################################################################################
#ver documentacion de REQUEST, RENDER y AUTH para logear y deslogear
#se puede usar un dbugger para ver que tipo de datos son el request.post() y el metodo request.method
#def login_view(request):
#    """Login view."""
#    if request.method == 'POST':
#        username = request.POST['username']
#        password = request.POST['password']
#        user = authenticate(request, username=username, password=password)
#        if user:
#            login(request, user)#
#
#            #REDIRECCIONA A UNA DETERMINADA URL
#            return redirect('posts:feed') #feed es el name='feed' del path de /posts/. Se puede usar ambas.
#        else:
#            return render(request, 'users/login.html', {'error': 'Invalid username and password'})#
#
#    return render(request, 'users/login.html') #REQUEST , 'ruta donde esta el template'
###########################################################################################################################
############################################################################################################
#Decorador para que no haga logout de una sesion inexistente
#@login_required
#def logout_view(request):
#    """Logout a user."""
#    logout(request)
#    return redirect('users:login') #login es el name='login'de /login_views/. Se puede usar ambas.
####################################################################################################################