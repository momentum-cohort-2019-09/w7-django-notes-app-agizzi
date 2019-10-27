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
    search_text = forms.CharField(label="Search Text", max_length=100)


class SortForm(forms.Form):
    by_title = forms.BooleanField(label="Sort By Title", required=False)
    CHOICES = [('Neither', 'Neither'), ('Descending', 'Descending'),
               ('Ascending', 'Ascending')]
    ascending_or_descending = forms.ChoiceField(choices=CHOICES)
