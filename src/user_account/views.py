from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView

from user_account.forms import UserAccountRegistrationForm, UserAccountProfileForm
from app import settings
from user_account.models import User


class CreateUserAccountView(CreateView):
    model = settings.AUTH_USER_MODEL
    template_name = 'user_account/registration.html'
    form_class = UserAccountRegistrationForm
    extra_context = {'title': 'Register new user'}
    success_url = reverse_lazy('account:login')

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['title'] = 'Register new user'
    #     return context
    #
    # def get_success_url(self):
    #     messages.success(self.request, "New user has been successfully created!")
    #     return reverse('account:login')

    def form_valid(self, form):
        result = super().form_valid(form)
        messages.success(self.request, "Great! New user has been successfully created!")
        return result


class UserAccountLoginView(LoginView):
    template_name = 'user_account/login.html'
    extra_context = {'title': 'Login as a user'}
    success_url = reverse_lazy('index')

    # def get_success_url(self):
    #     messages.success(self.request, "You've just successfully logged in")
    #     return reverse('index')

    def form_valid(self, form):
        result = super().form_valid(form)
        messages.success(self.request, "Great! You've just successfully logged in!")
        return result


class UserAccountLogoutView(LoginRequiredMixin, LogoutView):
    template_name = 'user_account/logout.html'
    extra_context = {'title': 'Logout from TESTS'}
    login_url = reverse_lazy('account:login')


class UserAccountProfileView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    template_name = 'user_account/profile.html'
    extra_context = {'title': 'Edit current user profile'}
    form_class = UserAccountProfileForm
    login_url = reverse_lazy('account:login')

    # def get_object(self, *args):
    #     return self.request.user

    def get_object(self, queryset=None):
        return self.request.user

    # def get_success_url(self):
    #     return reverse('account:profile')

    success_url = reverse_lazy('account:profile')
    success_message = "Your account has been updated!"
