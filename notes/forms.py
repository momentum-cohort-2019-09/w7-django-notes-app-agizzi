from django import forms
from notes.models import Note


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = [
            'title',
            'body',
        ]


class SearchForm(forms.Form):
    search_text = forms.CharField(max_length=100, label="search")


class SortForm(forms.Form):
    by_title = forms.BooleanField(label="Sort By Title", required=False)
    CHOICES = [('Neither', 'Neither'), ('Descending', 'Descending'),
               ('Ascending', 'Ascending')]
    ascending_or_descending = forms.ChoiceField(choices=CHOICES)
