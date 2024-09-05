from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView,FormView,TemplateView,DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView as AuthLoginView
from myapp.forms import EmailOrMobileAuthenticationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .forms import *
from django.contrib import messages
from .models import User
from django.core.mail import send_mail
from django.contrib.auth.views import PasswordResetView,PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin




# Create your views here.


class HomeView(TemplateView):
    template_name = 'myapp/home.html'

class SignupView(FormView):
    model=User
    template_name= 'myapp/signup.html'
    form_class = UserCreationForm
    success_url=reverse_lazy('myapp:details')

    def form_valid(self, form):
    # Validate and clean passwords using the form's validation methods
        password = form.cleaned_data.get('password')
        confirm_password = form.cleaned_data.get('confirm_password')

    # Check if passwords match
        if password and confirm_password and password != confirm_password:
            form.add_error('confirm_password', "Passwords do not match.")
            return self.form_invalid(form)

    # Save the user instance, but don't commit to the database yet
        user = form.save(commit=False)

    # Set the password using set_password to ensure it is hashed
        user.set_password(password)
        user.save()  # Now save the user to the database

    # Specify the custom authentication backend
        backend = 'myapp.backends.EmailOrMobileBackend'
    
    # Log the user in using the custom backend
        login(self.request, user, backend=backend)
    
    # Redirect to the success URL
        return redirect(self.success_url)

class LoginView(AuthLoginView):
    template_name = 'myapp/login.html'
    form_class = EmailOrMobileAuthenticationForm
    success_url = reverse_lazy('myapp:details')

    def form_valid(self, form):
        user = form.get_user()
        backend = 'myapp.backends.EmailOrMobileBackend'
        login(self.request, user, backend=backend)
        return redirect(self.success_url)



class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'myapp/password_reset.html'
    email_template_name = 'myapp/password_reset_email.html'
    subject_template_name = 'myapp/password_reset_subject'
    success_message = "We've emailed you instructions for setting your password, " \
                      "if an account exists with the email you entered. You should receive them shortly." \
                      " If you don't receive an email, " \
                      "please make sure you've entered the address you registered with, and check your spam folder."
    success_url = reverse_lazy('myapp:home')


class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'myapp/change_password.html'
    success_message = "Successfully Changed Your Password"
    success_url = reverse_lazy('myapp:home')

class DetailsView(TemplateView):
    template_name = 'myapp/details.html'
    success_url = reverse_lazy('myapp:job_status')

class JobStatusView(TemplateView):
    template_name = 'myapp/job_status.html'


class JobDetailsView(TemplateView):
    template_name = 'myapp/job_details.html'




class JobTitleView(TemplateView):
    template_name = 'myapp/job_title.html'


class RelationView(TemplateView):
    template_name = 'myapp/relationship_goals.html'


class InterestView(TemplateView):
    template_name = 'myapp/interested.html'

