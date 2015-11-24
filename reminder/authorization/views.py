from django.shortcuts import render, redirect
from django.core.context_processors import csrf
from django.contrib import auth
from django.contrib.auth.forms import AuthenticationForm
from django.core.urlresolvers import reverse

from .forms import UserCreateForm


def login(request):
    if request.user.is_authenticated():
        return redirect(reverse('note:all'))
    args = {}
    args.update(csrf(request))
    args['form'] = AuthenticationForm()
    if request.POST:
        user_post_form = AuthenticationForm(request, data=request.POST)
        if user_post_form.is_valid():
            user = user_post_form.get_user()
            auth.login(request, user)
            return redirect(reverse('note:all'))
        else:
            args['login_error'] = 'User is not find'

    return render(request, 'authorization/login.html', args)


def logout(request):
    auth.logout(request)
    return redirect(reverse('author:login'))


def registration(request):
    if request.user.is_authenticated():
        return redirect(reverse('note:all'))
    args = {}
    args.update(csrf(request))
    args['form'] = UserCreateForm()
    if request.POST:
        user_post_form = UserCreateForm(request.POST)
        if user_post_form.is_valid():
            user_post_form.save()
            new_user = auth.authenticate(
                username=user_post_form.cleaned_data['username'],
                password=user_post_form.cleaned_data['password2']
            )
            auth.login(request, new_user)
            return redirect(reverse('note:all'))
        else:
            args['form'] = user_post_form

    return render(request, 'authorization/registr.html', args)
