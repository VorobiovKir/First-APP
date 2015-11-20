from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib.auth import get_user
from django.contrib.auth.decorators import login_required

from .models import Notes, Categories, Tags
from .forms import AddNoteForm, AddTagForm, AddCategoryForm


@login_required(login_url='author:login')
def all(request):

    user = get_user(request)
    args = {}
    args['username'] = user.username.title()
    args['categories'] = Categories.objects.filter(author=user.id)
    args['alltags'] = Tags.objects.filter(author=user.id)
    args['form_note'] = AddNoteForm(user.id)
    args['form_tag'] = AddTagForm
    notes = Notes.objects.filter(author=user.id)
    # if not notes:
    #     return render(request, 'note/addNote.html', args)
    args['notes'] = notes

    return render(request, 'note/all.html', args)


@login_required(login_url='author:login')
def addNote(request):

    user = get_user(request)
    args = {}
    args['username'] = user.username.title()
    args['categories'] = Categories.objects.filter(author=user.id)
    args['alltags'] = Tags.objects.filter(author=user.id)
    args['form_note'] = AddNoteForm(user.id)
    # args['form_tag'] = AddTagForm
    # args['form_category'] = AddCategoryForm

    if request.POST:
        post_form = AddNoteForm(user.id, data=request.POST)
        if post_form.is_valid():
            post_form.save()

    return render(request, 'note/addNote.html', args)


@login_required(login_url='author:login')
def addCat(request):
    args = {}
    user = get_user(request)
    args['username'] = user.username.title()
    args['form_category'] = AddCategoryForm(user.id)

    if request.POST:
        post_form = AddCategoryForm(user.id, data=request.POST)
        if post_form.is_valid():
            post_form.save()

    return render(request, 'note/addCat.html', args)


@login_required(login_url='author:login')
def addTag(request):
    args = {}
    user = get_user(request)
    args['username'] = user.username.title()
    args['form_tag'] = AddTagForm

    return render(request, 'note/addTag.html', args)
