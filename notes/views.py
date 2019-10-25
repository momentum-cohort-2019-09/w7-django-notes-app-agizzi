from django.shortcuts import render, redirect, get_object_or_404
from notes.models import Note
from notes.forms import NoteForm, SearchForm, SortForm
from django.views.generic.edit import FormView
from django.db.models.functions import Coalesce
# Create your views here.


def notes_list(request):
    notes = Note.objects.all()
    return render(request, "notes/notes_list.html", {'notes': notes})


def note_details(request, pk):
    note = Note.objects.get(pk=pk)
    return render(request, "notes/notes_details.html", {'note': note})


def create_note(request):
    if request.method == "POST":  #form was submitted
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save()
            return redirect(to='notes_list')
    else:
        form = NoteForm()

    return render(request, "notes/create_note.html", {"form": form})


def edit_note(request, pk):
    note = get_object_or_404(Note, pk=pk)

    if request.method == "POST":
        form = NoteForm(instance=note, data=request.POST)
        if form.is_valid():
            note = form.save()
            return redirect(to='notes_details', pk=note.id)
    else:
        form = NoteForm(instance=note)

    return render(request, "notes/edit_note.html", {
        "note": note,
        "form": form,
    })


def delete_note(request, pk):
    note = get_object_or_404(Note, pk=pk)

    note.delete()
    notes = Note.objects.all()
    return render(request, 'notes/notes_list.html', {"notes": notes})


def search_notes(request):
    searched_notes = []
    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            notes = Note.objects.all()
            data = request.POST.copy()
            for note in notes:
                if data.get('search_text') in note.title:
                    searched_notes.append(note)
            return render(request, 'notes/search_results.html',
                          {'notes': searched_notes})
    else:
        form = SearchForm()
    return render(request, 'notes/search_notes.html', {'form': form})


def sort_notes(request):
    if request.method == "POST":
        unsorted_notes = Note.objects.annotate(
            last_touched=Coalesce('updated_at', 'created_at'))
        form = SortForm(request.POST)
        if form.is_valid():
            data = request.POST.copy()
            if data.get('by_title'):
                if data.get('ascending_or_descending') == 'Descending':
                    sorted_notes = unsorted_notes.order_by(
                        '-title', '-last_touched')
                elif data.get('ascending_or_descending') == 'Ascending':
                    sorted_notes = unsorted_notes.order_by(
                        'title', 'last_touched')
                elif data.get('ascending_or_descending') == 'Neither':
                    sorted_notes = unsorted_notes.order_by('title')
            else:
                if data.get('ascending_or_descending') == 'Descending':
                    sorted_notes = unsorted_notes.order_by('-last_touched')
                elif data.get('ascending_or_descending') == 'Ascending':
                    sorted_notes = unsorted_notes.order_by('last_touched')
        return render(request, 'notes/sorted_notes.html',
                      {'notes': sorted_notes})
    else:
        form = SortForm()
    return render(request, 'notes/sort_notes.html', {'form': form})
