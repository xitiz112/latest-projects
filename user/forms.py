# accounts/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from user.models import Training_plan



class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1', 'password2']

class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']



class Training_planForm(forms.ModelForm):
    class Meta:
        model = Training_plan
        fields = ['training_plan', 'current_weight', 'target_weight_category', 'sauna', 'swimming', 'private_trainer', 'private_coaching_hours']



