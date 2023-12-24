from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse_lazy
from .forms import UserCreationForm, LoginForm
from .models import CustomerUser
from django.contrib.auth import login, authenticate, logout


# class SignUpView(generic.CreateView):
#     form_class = CustomUserCreationForm
#     template_name = 'registration/signup.html'
#     success_url = reverse_lazy('login')

def signup(request):
    if request.user.is_authenticated:
        return redirect('cafemenu:home')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user_obj = CustomerUser.objects.create_user(
                form.cleaned_data['email'],
                form.cleaned_data['password1'],
                username=form.cleaned_data['email'],
                phone_number=form.cleaned_data['phone_number'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                birth_day=form.cleaned_data['birth_day'],
                city=form.cleaned_data['city'],
                address=form.cleaned_data['address'],
                image=form.cleaned_data['image'],
            )
            return redirect('cafemenu:home')
        else:
            print(form.errors)
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('cafemenu:home')
    else:
        form = LoginForm()

    return render(request, 'accounts/login.html', {'form': form})


def user_login(request):
    logout(request)
    return redirect('cafemenu:home')

