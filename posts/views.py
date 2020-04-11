"""Posts views."""

#from django.http import HttpResponse
#from datetime import datetime

#Django
#from django.shortcuts import render, redirect
#from django.contrib.auth.decorators import login_required #PARA QUE UNICAMENTE USUARIOS LOGEADOS PUEDEN VER ESTA URL POSTS
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DetailView, ListView
from django.urls import reverse_lazy


#Forms
from posts.forms import PostForm

#Models
from posts.models import Post
from posts.models import User

#Ver doc de LoginRequiredMixin (solo vean usuarios logeados)
#Ver doc de ListView
class PostsFeedView(LoginRequiredMixin, ListView):
    """Return all published posts."""

    template_name = 'posts/feed.html'
    model = Post
    ordering = ('-created',)
    paginate_by = 30
    context_object_name = 'posts'


#Para que muestre el detaill del usuario
#Ver url.py de Posts
class PostDetailView(LoginRequiredMixin, DetailView):
    """Return post detail."""

    template_name = 'posts/detail.html'
    queryset = Post.objects.all()
    context_object_name = 'post'


class CreatePostView(LoginRequiredMixin, CreateView):
    """Create a new post."""

    template_name = 'posts/new.hTml'
    form_class = PostForm
    success_url = reverse_lazy('posts:feed')

    def get_context_data(self, **kwargs):
        """Add user and profile to context."""
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['profile'] = self.request.user.profile
        return context
    

#PARA QUE UNICAMENTE USUARIOS LOGEADOS PUEDEN VER ESTA URL POSTS
#este decorador redireciona a la URL LOGIN_URL en setting.py al final.... 
#Nuestro LOGIN_URL es donde logearse (LOGIN_URL = '/users/login/')
#@login_required 
#def list_posts(request):
#    """List existing posts."""
    #Conectar los posts con el modelo Post. 
    #Post.objects es para conectar con el ORM
#    posts = Post.objects.all().order_by('-created')
    #encuentra el template porque en settings.py 'TEMPLATES' dice que busca en APP_DIR:True
#    return render(request, 'posts/feed.html', {'posts':posts}) #2do: el template. 3ro: es el contexto (lo que recibe)
    #busca el archivo en la carpeta del proyecto el templates y luego ingresa a posts y busca el feed.html


#@login_required
#def create_post(request):
#    """Create new post view."""

#    if request.method == 'POST':
#        form = PostForm(request.POST, request.FILES) #request.FILES para que los archivos de imagenes esten presentes
#
#        if form.is_valid():
#            form.save()
#            return redirect('posts:feed')
#
#    else:
#        form = PostForm() #Si el metodo no es POST, envia un post vacio.
#
#    return render(
#        request=request,
#        template_name='posts/new.html',
#        context={
#            'form': form,
#            'user': request.user,
#            'profile': request.user.profile
#            }
#        )