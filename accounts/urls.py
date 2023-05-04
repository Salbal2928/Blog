from django.urls import path
from .views import AccountCreate, AccountLogin, AccountLogout

app_name = 'accounts'

urlpatterns = [
    path('signup/', AccountCreate.as_view(), name='signup'),
    path('login/', AccountLogin.as_view(), name='login'),
    path('logout/', AccountLogout.as_view(), name='logout'),
]