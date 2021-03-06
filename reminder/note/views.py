from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib.auth import get_user
from django.contrib.auth.decorators import login_required

from .models import Notes, Categories, Tags
from .forms import AddNoteForm, AddTagForm, AddCategoryForm


@login_required(login_url='author:login')
def all(request, cat_id=None, tag_id=None):

    user = get_user(request)
    args = {}
    args['categories'] = Categories.objects.filter(author=user.id)
    args['all_tags'] = Tags.objects.filter(author=user.id)
    args['all_notes'] = Notes.objects.filter(author=user.id)
    args['form_note'] = AddNoteForm(user.id)
    args['form_tag'] = AddTagForm
    if cat_id:
        args['notes'] = Notes.objects.filter(author=user.id, category=cat_id)
    elif tag_id:
        args['notes'] = Notes.objects.filter(author=user.id, tag=tag_id)
    else:
        args['notes'] = args['all_notes']

    return render(request, 'note/all.html', args)


@login_required(login_url='author:login')
def addNote(request, note_id=None):

    user = get_user(request)
    args = {}
    args['categories'] = Categories.objects.filter(author=user.id)
    args['all_tags'] = Tags.objects.filter(author=user.id)
    if note_id:
        try:
            query = Notes.objects.get(pk=note_id, author=user.id)
        except Notes.DoesNotExist:
            return redirect(reverse('note:all'))
    else:
        query = None
    args['note_id'] = note_id
    args['form_note'] = AddNoteForm(user.id, instance=query)

    if request.POST:
        post_form = AddNoteForm(user.id, data=request.POST, instance=query)
        if post_form.is_valid():
            temp_save = post_form.save(commit=False)
            temp_save.author_id = user.id
            temp_save.save()
            post_form.save_m2m()
            return redirect(reverse('note:all'))

    return render(request, 'note/addNote.html', args)


@login_required(login_url='author:login')
def addCat(request, cat_id=None):

    args = {}
    user = get_user(request)
    args['categories'] = Categories.objects.filter(author=user.id)
    if cat_id:
        try:
            query = Categories.objects.get(id=cat_id, author=user.id)
        except Categories.DoesNotExist:
            return redirect(reverse('note:addCat'))
        args['form_category'] = AddCategoryForm(user.id, is_disabled=True, instance=query)
    else:
        query = None
        args['form_category'] = AddCategoryForm(user.id)

    args['cat_id'] = cat_id

    if request.POST:
        post_form = AddCategoryForm(user.id, data=request.POST, instance=query)
        if post_form.is_valid():
            post_form.save()
            return redirect(reverse('note:addCat'))

    return render(request, 'note/addCat.html', args)


@login_required(login_url='author:login')
def addTag(request, tag_id=None):

    args = {}
    user = get_user(request)
    args['tags'] = Tags.objects.filter(author=user.id)

    if tag_id:
        try:
            query = Tags.objects.get(id=tag_id, author=user.id)
        except Tags.DoesNotExist:
            return redirect(reverse('note:addTag'))
    else:
        query = None

    args['tag_id'] = tag_id
    args['form_tag'] = AddTagForm(user.id, instance=query)

    if request.POST:
        post_form = AddTagForm(user.id, data=request.POST, instance=query)
        if post_form.is_valid():
            post_form.save()

        return redirect(reverse('note:addTag'))

    return render(request, 'note/addTag.html', args)


@login_required(login_url='author:login')
def delNote(request, note_id):

    Notes.objects.get(pk=note_id).delete()

    return redirect(reverse('note:all'))


@login_required(login_url='author:login')
def delCat(request, cat_id):

    if request.POST:
        for cat_id in request.POST.getlist('remove_cat'):
            try:
                obj = Categories.objects.get(pk=cat_id)
                obj.delete()
            except Categories.DoesNotExist:
                continue

        return redirect(reverse('note:addCat'))
    else:
        Categories.objects.get(pk=cat_id).delete()

    return redirect(reverse('note:addCat'))


@login_required(login_url='author:login')
def delTag(request, tag_id):

    if request.POST:
        for tag_id in request.POST.getlist('remove_tag'):
            Tags.objects.get(pk=tag_id).delete()
        return redirect(reverse('note:addTag'))
    else:
        Tags.objects.get(pk=tag_id).delete()

    return redirect(reverse('note:addTag'))


def showCat(request, cat_id=None):
    user = get_user(request)
    args = {}
    args['notes'] = Notes.objects.filter(author=user.id, category=cat_id)

    return render(request, 'note/category.html', args)
