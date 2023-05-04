from django.views.generic  import (
    ListView, 
    DetailView, 
    CreateView,
    UpdateView,
    DeleteView,
    )
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from blogs.models import Blog
from django.urls import reverse_lazy
# Create your views here.

class BlogListView(LoginRequiredMixin, ListView):
    template_name = 'pages/bloglist.html'
    model = Blog
    context_object_name = 'blogs'
    

class BlogDetailView(LoginRequiredMixin,DetailView):
    template_name = 'pages/blogdetail.html'
    model = Blog
    context_object_name = 'blog'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        valid_author = str(self.request.user.get_username()) == str(self.get_object().author)
        context['author_validated'] = valid_author
        return context

class BlogCreateView(LoginRequiredMixin,CreateView):
    template_name = 'pages/blogcreate.html'
    model = Blog
    fields = ('title', 'content')
    success_url = reverse_lazy('pages:bloglist')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class BlogUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    template_name = 'pages/blogupdate.html'
    model = Blog
    fields = ('title', 'content')

    def get_success_url(self) -> str:
        return reverse_lazy('pages:blogdetail', kwargs={'pk':self.get_object().id})
    
    def test_func(self) -> bool | None:
        return self.get_object().author == self.request.user

class BlogDeleteView(LoginRequiredMixin,UserPassesTestMixin, DeleteView):
    template_name = 'pages/blogdelete.html'
    model = Blog
    success_url = reverse_lazy('pages:bloglist')

    def test_func(self) -> bool | None:
        return self.get_object().author == self.request.user
    