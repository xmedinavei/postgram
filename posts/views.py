"""Posts views."""
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.views.generic import CreateView, DetailView, ListView, DeleteView
from django.urls import reverse_lazy

#Forms
from posts.forms import PostForm

#Models
from posts.models import Post
from posts.models import User


class PostsFeedView(LoginRequiredMixin, ListView):
    """Return all published posts."""

    template_name = 'posts/feed.html'
    model = Post
    ordering = ('-created',)
    paginate_by = 30
    context_object_name = 'posts'


class PostDetailView(LoginRequiredMixin, DetailView):
    """Return post detail."""

    template_name = 'posts/detail.html'
    queryset = Post.objects.all()
    context_object_name = 'post'


class CreatePostView(LoginRequiredMixin, CreateView):
    """Create a new post."""

    template_name = 'posts/new.html'
    form_class = PostForm
    success_url = reverse_lazy('posts:feed')

    def get_context_data(self, **kwargs):
        """Add user and profile to context."""
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['profile'] = self.request.user.profile
        return context
    

class PostDeleteView(DeleteView):
    "Delete a post"
    print("You are about to delete a post, men!")
    # import pdb; pdb.set_trace()
    template_name = 'posts/delete.html'
    model = Post
    success_url = reverse_lazy('posts:feed')

    def get_queryset(self):
        queryset = super(PostDeleteView, self).get_queryset()
        # import pdb; pdb.set_trace()
        self.queryset = queryset.filter(id=self.kwargs['pk'])
        return self.queryset

    def get_object(self, queryset=None):
        return self.get_queryset()

    def post(self, *args, **kwargs):
        self.items_to_delete = self.request.POST.getlist('itemsToDelete')
        if self.request.POST.get("confirm_delete"):
            queryset = self.get_queryset()
            queryset.delete()
            return HttpResponseRedirect(self.success_url)
        elif self.request.POST.get("cancel"):
            return HttpResponseRedirect(self.success_url)
        else:
            return self.get(self, *args, **kwargs)