from django.shortcuts import render
from django.contrib.auth import login, get_user_model, logout

from django.http import HttpResponseRedirect
# Create your views here.
from .forms import UserCreationForm, UserLoginForm


def register(request, *args, **kwargs):
	form = UserCreationForm(request.POST or None)
	if form.is_valid():
		form.save()
		return HttpReponseRedirect('/login')
	context = {
		'form': form
	}
	return render(request, "accounts/register.html", context)


def login_view(request, *args, **kwargs):
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        user_obj = form.cleaned_data.get('user_obj')
        login(request, user_obj)
        return HttpResponseRedirect("/")
    return render(request, "accounts/login.html", {"form": form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect("/login")
