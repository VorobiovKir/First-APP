from django import forms

from .models import Notes, Tags, Categories

from mptt.forms import TreeNodeChoiceField



class AddNoteForm(forms.ModelForm):

    category = TreeNodeChoiceField(queryset=Categories.objects.none())
    tag = forms.ModelChoiceField(queryset=Tags.objects.none())

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(AddNoteForm, self).__init__(*args, **kwargs)
        self.fields['tag'].queryset = Tags.objects.filter(author=user)
        self.fields['category'].queryset = Categories.objects.filter(author=user)
        self.fields['category'].level_indicator = u'>>>'
        self.fields['category'].required = False
        self.fields['tag'].required = False


    class Meta:
        model = Notes
        fields = ['name', 'context', 'color', 'tag', 'category']


    def save(self, commit=True):
        note = super(AddNoteForm, self).save(commit=False)
        note.author_id = self.user
        if commit:
            note.save()
        return note


class AddTagForm(forms.ModelForm):

    class Meta:
        model = Tags
        fields = ['name']


class AddCategoryForm(forms.ModelForm):

    parent = TreeNodeChoiceField(Categories.objects.none(), required=False)

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(AddCategoryForm, self).__init__(*args, **kwargs)
        self.fields['parent'].queryset = Categories.objects.filter(author=user)
        self.fields['parent'].level_indicator = u'>>>'


    class Meta:
        model = Categories
        fields = ['name', 'parent']


    def save(self, commit=True):
        note = super(AddCategoryForm, self).save(commit=False)
        note.author_id = self.user
        if commit:
            note.save()
        return note
