from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email")

class LoginForm(AuthenticationForm):
    pass

class ProductSearchForm(forms.Form):
    keyword = forms.CharField(
        label="検索",
        required=False,
        widget=forms.TextInput(attrs={"placeholder":"商品を検索"})
    )