from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from django.forms import TextInput,PasswordInput

class CustomUserForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username','first_name','last_name']
        widgets = {
            'username':TextInput(attrs={
                'class':'form-control',
                'placeholder':'username'
            }),
            'first_name':TextInput(attrs={
                'class':'form-control',
                'placeholder':'firstname'
            }),
            'last_name':TextInput(attrs={
                'class':'form-control',
                'placeholder':'lastname'
            }),
        }

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ['username','first_name','last_name']
