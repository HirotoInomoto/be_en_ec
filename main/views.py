from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .forms import LoginForm, SignUpForm

class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = "main/signup.html"
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response

class Login(LoginView):
    authentication_form = LoginForm
    template_name = "main/login.html"

class Logout(LogoutView):
    pass