from django import forms

from .models import Notes, Tags, Categories

from mptt.forms import TreeNodeChoiceField


class AddNoteForm(forms.ModelForm):

    # category = TreeNodeChoiceField(queryset=Categories.objects.none(), required=False)
    # tag = forms.ModelChoiceField(queryset=Tags.objects.none(), required=False)

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(AddNoteForm, self).__init__(*args, **kwargs)
        # self.fields['tag'].queryset = Tags.objects.filter(author=user)
        # self.fields['category'].queryset = Categories.objects.filter(author=user)
        self.fields['category'].level_indicator = unichr(0x00A0) * 2
        # self.fields['category'].required = False
        # self.fields['tag'].required = False
        # self.fields['color'].required = False

    class Meta:
        model = Notes
        fields = ['name', 'context', 'color', 'tag', 'category']

    # def save(self, commit=True):
    #     test = Notes.objects.get(pk=self.user)
    #     note = super(AddNoteForm, self).save(commit=False)
    # #     test = note.save(commit=False)
    #     note.author_id = self.user
    # #     test.save()
    #
    #
    #     # note.category.add(Categories.object.get(id=note.category)
    #     # note.category.add(Categories.object.get(id=request.POST['category']))
    # #
    #     if commit:
    #         note.save()
    #         test.category.add(1)
    #         # self.save_m2m(commit=True)
    #         # note.category.add(Categories.objects.get(id=note.category))
    #         # note.save_m2m()
    #         # self.save_m2m()
    #         # return note


class AddTagForm(forms.ModelForm):

    class Meta:
        model = Tags
        fields = ['name']

    def __init__(self, user, *args, **kwargs):
        super(AddTagForm, self).__init__(*args, **kwargs)
        self.user = user

    def save(self, commit=True):
        note = super(AddTagForm, self).save(commit=False)
        note.author_id = self.user
        if commit:
            note.save()
        return note


class AddCategoryForm(forms.ModelForm):

    parent = TreeNodeChoiceField(Categories.objects.none(), required=False)

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(AddCategoryForm, self).__init__(*args, **kwargs)
        self.fields['parent'].queryset = Categories.objects.filter(author=user)
        self.fields['parent'].level_indicator = unichr(0x00A0) * 2

    class Meta:
        model = Categories
        fields = ['name', 'parent']

    def save(self, commit=True):
        note = super(AddCategoryForm, self).save(commit=False)
        note.author_id = self.user
        if commit:
            note.save()
        return note
