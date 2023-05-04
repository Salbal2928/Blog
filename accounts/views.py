from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from .forms import CustomUserForm

# Create your views here.
class AccountCreate(CreateView):
    form_class = CustomUserForm
    template_name = 'accounts/signup.html'
    
    def get_success_url(self) -> str:
        return reverse_lazy('accounts:login')

class AccountLogin(LoginView):
    redirect_authenticated_user = True
    template_name = 'accounts/login.html'

    def get_success_url(self) -> str:
        return reverse_lazy('pages:bloglist')
    
class AccountLogout(LogoutView):
    next_page = 'accounts:login'