from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import RegistrationForm, PaydayForm
from django.contrib.auth.decorators import login_required
from .models import Profile

# Create your views here.
def register(request):
    form = RegistrationForm(request.POST)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        messages.success(request, f"Welcome {username}! Your account has been created.")
        return redirect("registration")
    else:
        form = RegistrationForm()
    return render(request, 'users/register.html', {'form': form})

def registration(request):
    return render(request, 'users/registration.html')

@login_required
def profile(request):
    return render(request, 'users/profile.html')

@login_required
def update_payday(request, id):
    profile = Profile.objects.get(id=id)
    form = PaydayForm(request.POST or None, instance=profile)
    if form.is_valid():
        form.save()
        return redirect('profile')

    return render(request, 'users/payday-update.html', {'form': form, 'profile': profile})
