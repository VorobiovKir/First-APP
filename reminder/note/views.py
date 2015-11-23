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
    args['categories'] = Categories.objects.filter(author=user.id)
    args['all_tags'] = Tags.objects.filter(author=user.id)
    args['all_notes'] = Notes.objects.filter(author=user.id)
    args['form_note'] = AddNoteForm(user.id)
    args['form_tag'] = AddTagForm
    notes = Notes.objects.filter(author=user.id)
    # if not notes:
    #     return render(request, 'note/addNote.html', args)
    args['notes'] = notes

    # for category in args['categories']:
    #     print dir(category.notes_set)
    #     break

    return render(request, 'note/all.html', args)


@login_required(login_url='author:login')
def addNote(request):

    user = get_user(request)
    args = {}
    args['categories'] = Categories.objects.filter(author=user.id)
    args['all_tags'] = Tags.objects.filter(author=user.id)
    args['form_note'] = AddNoteForm(user.id)
    # args['form_tag'] = AddTagForm
    # args['form_category'] = AddCategoryForm

    if request.POST:
        post_form = AddNoteForm(user.id, data=request.POST)

        if post_form.is_valid():
            temp_save = post_form.save(commit=False)
            temp_save.author_id = user.id
            temp_save.save()
            post_form.save_m2m()
            # test = post_form.save(commit=False)
            # test.author_id = user.id
            # test.save()
            # post_form.save()
            # post_form.save_m2m()
            # post_form.save_m2m()
            # post_form.save()
            # post = Notes()
            # post.category.add(Categories.object.get(id=request.POST['category']))
            # post_form.save_m2m()

    return render(request, 'note/addNote.html', args)


@login_required(login_url='author:login')
def addCat(request):
    args = {}
    user = get_user(request)
    args['form_category'] = AddCategoryForm(user.id)
    args['categories'] = Categories.objects.filter(author=user.id)

    if request.POST:
        post_form = AddCategoryForm(user.id, data=request.POST)
        if post_form.is_valid():
            post_form.save()

    return render(request, 'note/addCat.html', args)


@login_required(login_url='author:login')
def addTag(request):
    args = {}
    user = get_user(request)
    args['form_tag'] = AddTagForm(user.id)

    if request.POST:
        post_form = AddTagForm(user.id, data=request.POST)

        if post_form.is_valid():
            post_form.save()

    return render(request, 'note/addTag.html', args)


@login_required(login_url='author:login')
def delNote(request, note_id):

    Notes.objects.get(pk=note_id).delete()

    return redirect(reverse('note:all'))
